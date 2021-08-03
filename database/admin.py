from django.contrib import admin
from . models import Database


class DatabaseAdmin(admin.ModelAdmin):
    list_display = ['name', 'config', 'edition',  'platform_id', 'version_id', 'organization_id', 'is_modif', 'is_active', 'check_backup']
    list_editable = ['is_modif', 'is_active', 'check_backup']
    list_filter = ['organization_id']


admin.site.register(Database, DatabaseAdmin)
