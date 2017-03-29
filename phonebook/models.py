from django.db import models

class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return "{0} {1}".format(self.first_name, self.last_name)

    class Meta:
    	permissions = (
    		("phonebook_download", u"Download phonebook via. basic authentication."),
    	)
