""""Бизнес-логика почтовой рассылки"""
from django.conf import settings
from django.core.mail import send_mail

from service.models import Mailing, Client


def send_email(mailing_id: str, ) -> bool:
    """Отправка email на указанный адрес и возвращает результат отправки"""
    mailing_item = Mailing.objects.get(pk=mailing_id)
    email_list = [cl for cl in mailing_item.clients.all()]

    send_mail(
        subject=f'{mailing_item.title}',
        message=f'{mailing_item.body}',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=email_list
    )

    return True
