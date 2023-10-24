from django.core.management import BaseCommand

from service.models import Mailing
from service.services import send_email


class Command(BaseCommand):

    def handle(self, *args, **options):
        """Запуск рассылки на все почтовые адреса через коммандную строку"""
        mailing_items = Mailing.objects.all()

        for item in mailing_items:
            email_list = [cl for cl in item.clients.all()]
            mailing_title = item.title
            mailing_body = item.body

            send_email(mailing_title, mailing_body, email_list)
