from django.db import models
from django.contrib import admin
from organization.models import Organization
from version1c.models import Version1C
from edition1c.models import Edition1C
from platform1c.models import Platfrom1C


class Database(models.Model):
    name = models.CharField(max_length=20, verbose_name='База данных')
    alias = models.CharField(max_length=20, verbose_name='Алиас базы', blank=True)
    organization_id = models.ForeignKey(Organization, on_delete=models.CASCADE, verbose_name='Организация')
    version_id = models.ForeignKey(Version1C, on_delete=models.CASCADE, null=True, verbose_name='Версия 1С')
    platform_id = models.ForeignKey(Platfrom1C, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Платформа 1С')
    edition = models.ForeignKey(Edition1C, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Редакция 1С')
    date_backup = models.DateField(blank=True, null=True, verbose_name='Дата проверки бэкапа')
    check_backup = models.BooleanField(blank=True, default=True, verbose_name='Контроллировать бэкап')
    is_modif = models.BooleanField(default=False, verbose_name='Доработки')
    is_active = models.BooleanField(default=True, verbose_name='Активность')

    def __str__(self):
        return self.name

    @admin.display(description='Конфигурация 1С')
    def config(self):
        return self.version_id.config_id

    class Meta:
        verbose_name = 'База данных'
        verbose_name_plural = 'Базы данных'
        ordering = ['organization_id', 'name']
