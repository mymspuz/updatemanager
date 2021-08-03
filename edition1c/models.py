from django.db import models
from config1c.models import Config1C


class Edition1C(models.Model):
    name = models.CharField(max_length=50, verbose_name='Редакция')
    config = models.ManyToManyField(Config1C, verbose_name='Конфигурация 1С')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Редакция 1С'
        verbose_name_plural = 'Редакции'
        ordering = ['name']
