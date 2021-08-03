from django.contrib import admin
from . models import Edition1C


class Edition1CAdmin(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(Edition1C, Edition1CAdmin)

