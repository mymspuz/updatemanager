from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User


class Organization(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Организация')
    description = models.CharField(max_length=150, blank=True, verbose_name='Описание')
    picture = models.ImageField(upload_to='', blank=True, verbose_name='Изображение')
    is_active = models.BooleanField(default=True, verbose_name='Активность')
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')

    @admin.display(description='Кол-во БД')
    def count_db(self):
        from database.models import Database
        return Database.objects.filter(organization_id=self).count()

    @admin.display(description='Есть БД', boolean=True)
    def is_db(self):
        from database.models import Database
        count = Database.objects.filter(organization_id=self).count()
        return True if count else False

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Организация'
        verbose_name_plural = 'Организации'
        ordering = ['name']
