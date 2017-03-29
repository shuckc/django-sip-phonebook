from django.contrib import admin

from .models import Contact
import datetime

class ContactAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname', 'phone_number')

admin.site.register(Contact, ContactAdmin)
