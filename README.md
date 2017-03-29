# django-sip-phonebook
A django-powered central phonebook and provisioning server for Grandstream telephones

[![PyPi packaged](https://badge.fury.io/py/django-sip-phonebook.svg)](http://badge.fury.io/py/django-sip-phonebook)


Quick start
-----------

1. Add "phonebook" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'phonebook',
    ]

2. Include the phonebook URLconf in your project urls.py like this::

    url(r'^phonebook/', include('phonebook.urls')),

3. Run `python manage.py migrate` to create the phonebook models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to setup phone book entries (you'll need the Admin app enabled).

5. Setup your Grandstream IP phone to fetch it's phonebook from http://127.0.0.1:8000 
   and verify you can call the contacts you added.

