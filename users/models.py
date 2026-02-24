from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='почта')
    phone_number = models.CharField(max_length=16, blank=True, null=True, verbose_name='номер телефона')
    country = models.CharField(verbose_name='страна')
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True, verbose_name='аватар')
    token = models.CharField(max_length=100, verbose_name="Token", blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'


    def __str__(self):
        return self.email
