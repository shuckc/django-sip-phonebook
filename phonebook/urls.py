from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^gs_phonebook.xml$', views.phonebook, name='phonebook'),
]
