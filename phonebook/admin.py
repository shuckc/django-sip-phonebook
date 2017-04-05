from django.contrib import admin

from .models import Contact, Group
import datetime

class ContactAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phone_number', 'job_title', 'group')
    list_filter = ('group',)
    list_select_related = ('group',)

class GroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'index')

admin.site.register(Contact, ContactAdmin)
admin.site.register(Group, GroupAdmin)
