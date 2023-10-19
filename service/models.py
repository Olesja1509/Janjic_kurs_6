from datetime import datetime

from django.conf import settings
from django.db import models
from django.utils import timezone

NULLABLE = {'blank': True, 'null': True}


# def default_datetime():
#     return datetime.now()


class Client(models.Model):
    email = models.EmailField(verbose_name='почта')
    first_name = models.CharField(max_length=50, verbose_name='Имя', **NULLABLE)
    last_name = models.CharField(max_length=50, verbose_name='Фамилия', **NULLABLE)
    comment = models.TextField(verbose_name='Комментарий', **NULLABLE)

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, verbose_name='Пользователь',
                             **NULLABLE)

    def __str__(self):
        return f'{self.email} ({self.first_name} {self.last_name})'

    class Meta:
        verbose_name = 'клиент'
        verbose_name_plural = 'клиенты'


class Mailing(models.Model):

    # STATUS = (
    #     ('finished', 'завершена'),
    #     ('created', 'создана'),
    #     ('started', 'запущена')
    # )

    PERIOD = (
        ('daily', 'раз в день'),
        ('weekly', 'раз в неделю'),
        ('monthly', 'раз в месяц')
    )

    title = models.CharField(max_length=50, verbose_name='Тема рассылки', unique=True)
    body = models.TextField(verbose_name='Тело письма')
    start_time = models.DateTimeField(verbose_name='Время начала')
    finish_time = models.DateTimeField(verbose_name='Время окончания')
    period = models.CharField(max_length=10, choices=PERIOD, verbose_name='Периодичность рассылки')
    status = models.CharField(max_length=10, verbose_name='Статус рассылки', **NULLABLE)
    clients = models.ManyToManyField(Client, **NULLABLE)

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, verbose_name='Пользователь',
                             **NULLABLE)

    def save(self, *args, **kwargs):
        if self.finish_time < timezone.now():
            self.status = 'завершена'
        elif self.start_time > timezone.now():
            self.status = 'создана'
        else:
            self.status = 'запущена'
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'рассылка'
        verbose_name_plural = 'рассылки'


class Logs(models.Model):

    STATUS = (
        ('Not_sent', 'Не отправлено'),
        ('Departure', 'Отправляется'),
        ('Sent', 'Отправлено')
    )

    title = models.ForeignKey(Mailing, on_delete=models.CASCADE, verbose_name='Тема рассылки')
    email = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name='почта', **NULLABLE)
    time = models.DateTimeField(verbose_name='Дата и время последней попытки')
    status = models.CharField(max_length=10, choices=STATUS, verbose_name='Статус попытки')
    period = models.CharField(max_length=50, verbose_name='Ответ почтового сервиса', **NULLABLE)

    class Meta:
        verbose_name = 'лог'
        verbose_name_plural = 'логи'

