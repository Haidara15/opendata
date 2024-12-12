from django.contrib import admin

from .models import Datatable


class DatatableAdmin(admin.ModelAdmin):
    list_display = ('periodicite','data')
admin.site.register(Datatable, DatatableAdmin)