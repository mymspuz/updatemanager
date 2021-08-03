from django.db import models
from config1c.models import Config1C
from platform1c.models import Platfrom1C


class Version1C(models.Model):
    name = models.CharField(max_length=25, verbose_name='Версия 1С')
    config_id = models.ForeignKey(Config1C,
                                  on_delete=models.CASCADE,
                                  blank=True,
                                  null=True,
                                  verbose_name='Конфигурация 1С'
                                  )
    platform_id = models.ManyToManyField(Platfrom1C, verbose_name='Платформа 1С')
    date = models.DateField(verbose_name='Дата релиза', blank=True, null=True)
    connection = models.TextField(null=True, blank=True, verbose_name='Обновление версии')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Версия 1С'
        verbose_name_plural = 'Версии'
        ordering = ['-date', 'name', 'config_id']
