from django.db import models
from django.conf import settings
from django.core.urlresolvers import reverse

from tenants.models import Property

# Create your models here.
	

class Resume(models.Model):
	name = models.CharField(max_length = 20)
	# Change docfile name to resume
	docfile = models.FileField(upload_to='resumes/')


	def __unicode__(self):
		return self.name

class DocQuerySet(models.query.QuerySet):

	def user(self):
		return self.filter(user=user)

	def investor(self):
		return self.filter(catagory='Investor')
		
	def tenant(self):
		return self.filter(catagory='Tenant')

	def news(self):
		return self.filter(catagory='News')
		
	
class DocManager(models.Manager):
	def get_queryset(self):
		return DocQuerySet(self.model, using=self._db)

	def investor(self):
		return self.get_queryset().investor()

	def tenant(self):
		return self.get_queryset().tenant()

	def news(self):
		return self.get_queryset().news()


# Dept cat
DOC_CATEGORIES = (
	('Investor', 'Investor'),
	('Tenant', 'Tenant'),
	('News', 'News'),
)


class Document(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, null = True, blank = True)
	prop = models.ForeignKey(Property, null = True, blank = True)
	name = models.CharField(max_length = 50, unique = True)
	# change docfile name to document
	docfile = models.FileField(upload_to='documents/')
	catagory = models.CharField(max_length = 120, choices = DOC_CATEGORIES, null = True, blank = True)
	timestamp = models.DateTimeField(auto_now_add = True, auto_now = False)
	brochure = models.BooleanField(default=False)
	objects = DocManager()

	def get_date(self):
		return self.timestamp.date()

	def get_absolute_url(self):
		return reverse("download", kwargs = {"name": self.name,})


	def __unicode__(self):
		if self.prop:
			return str(self.name) + ' ' + str(self.prop.name)
		else:
			return self.name

class GenericImage(models.Model):
	name = models.CharField(max_length=100, null = True, blank = True)
	image = models.ImageField(upload_to = settings.MEDIA_ROOT)

	def __unicode__(self):
		return self.name


