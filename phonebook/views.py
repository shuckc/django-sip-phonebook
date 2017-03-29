from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse

from .models import Contact

from django_basic_auth import has_perm_or_basicauth

@has_perm_or_basicauth('phonebook.phonebook_download')
def phonebook(request):
    contacts = Contact.objects.all()
    return render(request, 'phonebook/names.xml', {
        'contacts': contacts,
    })
