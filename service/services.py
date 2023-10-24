""""Бизнес-логика почтовой рассылки"""
from smtplib import SMTPException

from django.conf import settings
from django.core.mail import send_mail
from django.utils import timezone
from django_apscheduler.util import close_old_connections

from service.models import Logs


@close_old_connections
def send_email(mailing_title, mailing_body, email_list):
    """Отправляет email на указанные адреса"""

    for client in email_list:
        try:
            send_mail(
                subject=mailing_title,
                message=mailing_body,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=email_list,
                fail_silently=False,
            )

            Logs.objects.create(
                title=mailing_title,
                email=client,
                time=timezone.now(),
                status='Отправлено'
            )

        except SMTPException:
            Logs.objects.create(
                title=mailing_title,
                email=client,
                time=timezone.now(),
                status='Не отправлено'
            )
