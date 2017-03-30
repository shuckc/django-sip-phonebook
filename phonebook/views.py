from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse

from .models import Contact, Group

from django_basic_auth import has_perm_or_basicauth

@has_perm_or_basicauth('phonebook.phonebook_download')
def phonebook(request):
    groups = Group.objects.all()
    contacts = Contact.objects.all()
    return render(request, 'phonebook/names.xml', {
        'contacts': contacts,
        'groups': groups,
    })
