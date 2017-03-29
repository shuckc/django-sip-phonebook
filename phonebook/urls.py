from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^phonebook.xml$', views.phonebook, name='phonebook'),
]
