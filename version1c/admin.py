from django.contrib import admin
from . models import Version1C


class Version1CAdmin(admin.ModelAdmin):
    list_display = ['name', 'config_id', 'date']
    list_filter = ['config_id']


admin.site.register(Version1C, Version1CAdmin)