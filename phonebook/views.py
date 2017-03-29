from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse

from .models import Contact

from django_basic_auth import logged_in_or_basicauth

@logged_in_or_basicauth
def phonebook(request):
    contacts = Contact.objects.all()
    return render(request, 'phonebook/names.xml', {
        'contacts': contacts,
    })
