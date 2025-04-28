from django.contrib import admin

from .models import ContactRequest

class ContactRequestAdmin(admin.ModelAdmin):

    list_display = [field.name for field in ContactRequest._meta.fields]

admin.site.register(ContactRequest, ContactRequestAdmin)
