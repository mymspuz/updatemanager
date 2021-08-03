from django.contrib import admin
from . models import Organization


class OrganizationAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'picture', 'is_active', 'count_db', 'is_db']
    list_display_links = ['name']
    list_filter = ['is_active']
    list_editable = ['is_active']
    search_fields = ['name']


admin.site.register(Organization, OrganizationAdmin)
