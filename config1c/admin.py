from django.contrib import admin
from . models import Config1C


class Config1CAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']


admin.site.register(Config1C, Config1CAdmin)