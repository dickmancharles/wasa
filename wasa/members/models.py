from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.

class MemberQuerySet(models.query.QuerySet):
	def prin(self):
		return self.filter(department='Executive Committee')
		
	def executive(self):
		return self.filter(department='Key Personnel')
		

class DeptManager(models.Manager):
	def get_queryset(self):
		return MemberQuerySet(self.model, using=self._db)

	def prin(self):
		return self.get_queryset().prin()

	def executive(self):
		return self.get_queryset().executive()


# Dept cat
DEPT_CATEGORIES = (
	('Executive Committee', 'Executive Committee'),
	('Key Personnel', 'Key Personnel'),
)

# change class name to staff & staff images / Add Address for single page display
class StaffMember(models.Model): 
	name = models.CharField(max_length = 50)
	title = models.CharField(max_length = 50)
	department = models.CharField(max_length = 120, choices = DEPT_CATEGORIES, default = '')
	description = models.TextField(max_length = 2000, null = True, blank = True)
	email = models.EmailField() 
	work_phone = models.CharField(max_length = 50, null = True, blank = True)
	under_grad_school = models.CharField(max_length = 150, null = True, blank = True)
	under_grad_degree = models.CharField(max_length = 150, null = True, blank = True)
	grad_school = models.CharField(max_length = 150, null = True, blank = True)
	grad_degree = models.CharField(max_length = 150, null = True, blank = True)
	street_address = models.CharField(max_length = 120, null = True, blank = True)
	city = models.CharField(max_length = 150, null = True, blank = True)
	slug = models.SlugField(unique = True)

	objects = DeptManager()

	def __unicode__(self):
	 	return self.name
	 	

	class Meta:
		unique_together = ('name', 'slug')



class StaffMemberImage(models.Model):
	member = models.ForeignKey(StaffMember)
	image = models.ImageField(upload_to= 'members/')

	def __unicode__(self):
		return self.member.name
		
class Position(models.Model):
	position = models.CharField(max_length = 50)
	division = models.CharField(max_length = 50)
	location = models.CharField(max_length = 50)
	salary = models.CharField(max_length = 50, null = True, blank = True)
	description = models.TextField(max_length = 1000)

	def __unicode__(self):
		return self.position


		
		