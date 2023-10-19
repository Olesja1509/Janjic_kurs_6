from django.conf import settings
from django.core.mail import send_mail
from django.core.management import BaseCommand

from service.models import Mailing, Client


class Command(BaseCommand):

    def handle(self, *args, **options):
        """Запуск рассылки на все почтовые адреса через коммандную строку"""
        mailing_items = Mailing.objects.all()

        for item in mailing_items:
            email_list = [cl for cl in item.clients.all()]

            send_mail(
                f'{item.title}',
                f'{item.body}',
                settings.EMAIL_HOST_USER,
                email_list
            )
