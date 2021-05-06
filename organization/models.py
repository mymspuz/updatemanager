from django.db import models
from django.contrib.auth.models import User


class Organization(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Организация')
    description = models.CharField(max_length=150, blank=True, verbose_name='Описание')
    picture = models.ImageField(upload_to='', verbose_name='Изображение')
    is_active = models.BooleanField(default=True, verbose_name='Активность')
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')

    def __str__(self):
        return self.name
