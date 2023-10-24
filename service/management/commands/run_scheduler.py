import logging

from apscheduler.triggers.cron import CronTrigger
from django.core.management.base import BaseCommand
from django_apscheduler.models import DjangoJobExecution
from django_apscheduler import util

from config.mailing_scheduler import scheduler
from service.models import Mailing
from service.services import send_email

logger = logging.getLogger(__name__)


# The `close_old_connections` decorator ensures that database connections, that have become
# unusable or are obsolete, are closed before and after your job has run. You should use it
# to wrap any jobs that you schedule that access the Django database in any way. 
@util.close_old_connections
def delete_old_job_executions(max_age=604_800):
    """
    This job deletes APScheduler job execution entries older than `max_age` from the database.
    It helps to prevent the database from filling up with old historical records that are no
    longer useful.

    :param max_age: The maximum length of time to retain historical job execution records.
                    Defaults to 7 days.
    """
    DjangoJobExecution.objects.delete_old_job_executions(max_age)


class Command(BaseCommand):
    help = "Runs APScheduler."

    def handle(self, *args, **options):

        mailing_items = Mailing.objects.all()
        for item in mailing_items:
            mailing_title = item.title
            mailing_body = item.body
            email_list = [cl for cl in item.clients.all()]

            if item.period == 'daily':
                trigger = CronTrigger(hour='0', minute='00', start_date=item.start_time, end_date=item.finish_time)
            elif item.period == 'weekly':
                trigger = CronTrigger(day_of_week='mon', hour='9', start_date=item.start_time, end_date=item.finish_time)
            elif item.period == 'monthly':
                trigger = CronTrigger(day='1', hour='9', start_date=item.start_time, end_date=item.finish_time)

            scheduler.add_job(
                send_email,
                kwargs={'mailing_title': mailing_title, 'mailing_body': mailing_body, 'email_list': email_list},
                trigger=trigger,
                id=f'mailing_{item.title}',
                max_instances=1,
                replace_existing=True,
            )

            logger.info(f"Added job {item.title}.")

            scheduler.add_job(
                delete_old_job_executions,
                trigger=CronTrigger(
                    day_of_week="mon", hour="00", minute="00"
                ),  # Midnight on Monday, before start of the next work week.
                id="delete_old_job_executions",
                max_instances=1,
                replace_existing=True,
            )
            logger.info(
                "Added weekly job: 'delete_old_job_executions'."
            )

        try:
            logger.info("Starting scheduler...")
            scheduler.start()
        except KeyboardInterrupt:
            logger.info("Stopping scheduler...")
            scheduler.shutdown()
            logger.info("Scheduler shut down successfully!")
