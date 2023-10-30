from django.contrib.auth.models import AbstractUser
from django.db import models


NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    username = None
    email = models.EmailField(verbose_name='почта', unique=True)

    phone = models.CharField(max_length=35, verbose_name='телефон', **NULLABLE)
    country = models.CharField(max_length=50, verbose_name='страна', **NULLABLE)

    is_active = models.BooleanField(default=False)
    verification_code = models.CharField(max_length=40, **NULLABLE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
