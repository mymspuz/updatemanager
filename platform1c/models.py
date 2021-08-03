from django.db import models


class Platfrom1C(models.Model):
    name = models.CharField(max_length=20, verbose_name='Платформа 1С')
    description = models.CharField(max_length=150, blank=True, verbose_name='Описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Платформа'
        verbose_name_plural = 'Платформы'
        ordering = ['name']
