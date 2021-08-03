from django.contrib import admin
from . models import Platfrom1C


class Platform1CAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_display_links = ['name']
    search_fields = ['name']


admin.site.register(Platfrom1C, Platform1CAdmin)
