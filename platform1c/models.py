from django.db import models

class Platfrom1C(models.Model):
    name = models.CharField(max_length=20, verbose_name='Платформа')
    description = models.CharField(max_length=150, verbose_name='Описание')

    def __str__(self):
        return self.name