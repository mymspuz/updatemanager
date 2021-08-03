from django.db import models


class Config1C(models.Model):
    name = models.CharField(max_length=100, verbose_name='Конфигурация 1С')
    description = models.CharField(max_length=150, blank=True, verbose_name='Описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Конфигурация 1С'
        verbose_name_plural = 'Конфигурации 1С'
        ordering = ['name']
