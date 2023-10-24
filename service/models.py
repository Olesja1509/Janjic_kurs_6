from datetime import datetime

from django.conf import settings
from django.db import models
from django.utils import timezone

NULLABLE = {'blank': True, 'null': True}


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

    PERIOD = (
        ('daily', 'раз в день'),
        ('weekly', 'раз в неделю'),
        ('monthly', 'раз в месяц')
    )

    title = models.CharField(max_length=50, verbose_name='Тема рассылки', unique=True)
    body = models.TextField(verbose_name='Тело письма')
    start_time = models.DateTimeField(verbose_name='Время начала', default=datetime.today())
    finish_time = models.DateTimeField(verbose_name='Время окончания')
    period = models.CharField(max_length=10, choices=PERIOD, verbose_name='Периодичность рассылки')
    status = models.CharField(max_length=10, verbose_name='Статус рассылки', **NULLABLE)
    is_active = models.BooleanField(verbose_name='Отметка об активности')
    clients = models.ManyToManyField(Client, verbose_name='Клиенты')

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, verbose_name='Пользователь',
                             **NULLABLE)

    def save(self, *args, **kwargs):
        if self.finish_time < timezone.now():
            self.status = 'завершена'
            self.is_active = False
        elif self.start_time > timezone.now():
            self.status = 'создана'
            self.is_active = True
        else:
            self.status = 'запущена'
            self.is_active = True

        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'рассылка'
        verbose_name_plural = 'рассылки'


class Logs(models.Model):

    title = models.CharField(max_length=50, verbose_name='Тема рассылки')
    email = models.EmailField(verbose_name='почта', **NULLABLE)
    time = models.DateTimeField(verbose_name='Дата и время последней попытки')
    status = models.CharField(max_length=10, verbose_name='Статус попытки')

    class Meta:
        verbose_name = 'лог'
        verbose_name_plural = 'логи'
