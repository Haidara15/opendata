from django.contrib import admin

from .models import Actualite


class ActualiteAdmin(admin.ModelAdmin):
    
    list_display = [field.name for field in Actualite._meta.fields]

admin.site.register(Actualite, ActualiteAdmin)
