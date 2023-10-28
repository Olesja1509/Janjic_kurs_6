from apscheduler.schedulers.blocking import BlockingScheduler
from django.conf import settings
from django_apscheduler.jobstores import DjangoJobStore


scheduler = BlockingScheduler(timezone=settings.TIME_ZONE)

scheduler.add_jobstore(DjangoJobStore(), 'default')
