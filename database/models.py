from django.db import models
from organization.models import Organization


class Database(models.Model):
    name = models.CharField(max_length=20, verbose_name='База данных')
    organization_id = models.ForeignKey(Organization, on_delete=models.CASCADE, verbose_name='Организация')
    is_active = models.BooleanField(default=True, verbose_name='Активность')

    def __str__(self):
        return self.name
