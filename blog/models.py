from datetime import datetime

from django.db import models

NULLABLE = {'blank': True, 'null': True}


def default_datetime():
    return datetime.now()


class Article(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    body = models.TextField(verbose_name='Содержимое статьи')
    preview = models.ImageField(upload_to='articles/', verbose_name='Изображение', **NULLABLE)
    creation_date = models.DateTimeField(verbose_name='Дата публикации', default=default_datetime)
    views = models.IntegerField(verbose_name='Количество просмотров', default=0)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'статья'
        verbose_name_plural = 'статьи'

