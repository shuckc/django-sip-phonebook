from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

from .models import Contact

def phonebook(request):
    contacts = Contact.objects.all()
    return render(request, 'phonebook/names.xml', {
        'contacts': contacts,
    })
