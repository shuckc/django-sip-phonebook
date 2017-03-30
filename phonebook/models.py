from django.db import models

class Group(models.Model):
	name = models.CharField(max_length=10)
	index = models.PositiveSmallIntegerField(unique=True)

	def __str__(self):
		return "{0}".format(self.name)

class Contact(models.Model):
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	phone_number = models.CharField(max_length=100, blank=True)
	job_title = models.CharField(max_length=100, blank=True)
	group = models.ForeignKey(Group, blank=True, null=True)

	def __str__(self):
		return "{0} {1}".format(self.first_name, self.last_name)

	class Meta:
		permissions = (
			("phonebook_download", u"Download phonebook via. basic authentication."),
		)
