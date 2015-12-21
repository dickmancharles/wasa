from django.db import models

# Create your models here.
class CompanyProfile(models.Model):
	text = models.TextField(max_length = 1500, null = True, blank = True)

	def __unicode__(self):
		return 'Company Profile'

class OwnersRep(models.Model):
	text_left_side = models.TextField(max_length = 2500, null = True, blank = True)
	bulletpoint_title = models.CharField(max_length = 200, null = True, blank = True)
	bulletpoint1 = models.CharField(max_length = 100, null = True, blank = True)
	bulletpoint2 = models.CharField(max_length = 100, null = True, blank = True)
	bulletpoint3 = models.CharField(max_length = 100, null = True, blank = True)
	bulletpoint4 = models.CharField(max_length = 100, null = True, blank = True)
	bulletpoint5 = models.CharField(max_length = 100, null = True, blank = True)
	bulletpoint6 = models.CharField(max_length = 100, null = True, blank = True)
	bulletpoint7 = models.CharField(max_length = 100, null = True, blank = True)
	bulletpoint8 = models.CharField(max_length = 100, null = True, blank = True)
	bulletpoint9 = models.CharField(max_length = 100, null = True, blank = True)


	def __unicode__(self):
		return 'OwnersRep'


class AcquisitionPage(models.Model):
	retail = models.TextField(max_length = 1500, null = True, blank = True)
	retail_title = models.CharField(max_length = 200, null = True, blank = True)
	retailpoint1 = models.CharField(max_length = 100, null = True, blank = True)
	retailpoint2 = models.CharField(max_length = 100, null = True, blank = True)
	retailpoint3 = models.CharField(max_length = 100, null = True, blank = True)
	retailpoint4 = models.CharField(max_length = 100, null = True, blank = True)
	retailpoint5 = models.CharField(max_length = 100, null = True, blank = True)
	retailpoint6 = models.CharField(max_length = 100, null = True, blank = True)
	retailpoint7 = models.CharField(max_length = 100, null = True, blank = True)
	retailpoint8 = models.CharField(max_length = 100, null = True, blank = True)
	retailpoint9 = models.CharField(max_length = 100, null = True, blank = True)


	types_of_deals_title = models.CharField(max_length = 200, null = True, blank = True)
	dealspoint1 = models.CharField(max_length = 100, null = True, blank = True)
	dealspoint2 = models.CharField(max_length = 100, null = True, blank = True)
	dealspoint3 = models.CharField(max_length = 100, null = True, blank = True)
	dealspoint4 = models.CharField(max_length = 100, null = True, blank = True)
	dealspoint5 = models.CharField(max_length = 100, null = True, blank = True)
	dealspoint6 = models.CharField(max_length = 100, null = True, blank = True)
	dealspoint7 = models.CharField(max_length = 100, null = True, blank = True)
	dealspoint8 = models.CharField(max_length = 100, null = True, blank = True)
	dealspoint9 = models.CharField(max_length = 100, null = True, blank = True)

	submission_critera_title = models.CharField(max_length = 200, null = True, blank = True)
	criterapoint1 = models.CharField(max_length = 100, null = True, blank = True)
	criterapoint2 = models.CharField(max_length = 100, null = True, blank = True)
	criterapoint3 = models.CharField(max_length = 100, null = True, blank = True)
	criterapoint4 = models.CharField(max_length = 100, null = True, blank = True)
	criterapoint5 = models.CharField(max_length = 100, null = True, blank = True)
	criterapoint6 = models.CharField(max_length = 100, null = True, blank = True)
	criterapoint7 = models.CharField(max_length = 100, null = True, blank = True)
	criterapoint8 = models.CharField(max_length = 100, null = True, blank = True)
	criterapoint9 = models.CharField(max_length = 100, null = True, blank = True)

	acquisitions_person_name1 = models.CharField(max_length = 200, null = True, blank = True)
	acquisitions_person_title1 = models.CharField(max_length = 200, null = True, blank = True)
	phonenumber1 = models.CharField(max_length = 200, null = True, blank = True)
	fax1 = models.CharField(max_length = 200, null = True, blank = True)
	email1 = models.CharField(max_length = 200, null = True, blank = True)

	acquisitions_person_name2 = models.CharField(max_length = 200, null = True, blank = True)
	acquisitions_person_title2 = models.CharField(max_length = 200, null = True, blank = True)
	phonenumber2 = models.CharField(max_length = 200, null = True, blank = True)
	fax2 = models.CharField(max_length = 200, null = True, blank = True)
	email2 = models.CharField(max_length = 200, null = True, blank = True)

	def __unicode__(self):
		return 'Acquisition'

class Career(models.Model):
	health_care_insurace_title = models.CharField(max_length = 50, null = True, blank = True)

	healthcarepoint1 = models.CharField(max_length = 100, null = True, blank = True)
	healthcarepoint2 = models.CharField(max_length = 100, null = True, blank = True)
	healthcarepoint3 = models.CharField(max_length = 100, null = True, blank = True)
	healthcarepoint4 = models.CharField(max_length = 100, null = True, blank = True)
	healthcarepoint5 = models.CharField(max_length = 100, null = True, blank = True)
	healthcarepoint6 = models.CharField(max_length = 100, null = True, blank = True)
	healthcarepoint7 = models.CharField(max_length = 100, null = True, blank = True)
	healthcarepoint8 = models.CharField(max_length = 100, null = True, blank = True)
	healthcarepoint9 = models.CharField(max_length = 100, null = True, blank = True)

	retirement_tax_programs = models.CharField(max_length = 200, null = True, blank = True)
	taxpoint1 = models.CharField(max_length = 100, null = True, blank = True)
	taxpoint2 = models.CharField(max_length = 100, null = True, blank = True)
	taxpoint3 = models.CharField(max_length = 100, null = True, blank = True)
	taxpoint4 = models.CharField(max_length = 100, null = True, blank = True)
	taxpoint5 = models.CharField(max_length = 100, null = True, blank = True)
	taxpoint6 = models.CharField(max_length = 100, null = True, blank = True)
	taxpoint7 = models.CharField(max_length = 100, null = True, blank = True)
	taxpoint8 = models.CharField(max_length = 100, null = True, blank = True)
	taxpoint9 = models.CharField(max_length = 100, null = True, blank = True)

	students_title = models.CharField(max_length = 200, null = True, blank = True)
	students_text = models.TextField(max_length = 500, null = True, blank = True)

	def __unicode__(self):
		return 'Career'

class HelpCenter(models.Model):

	header_1 = models.CharField(max_length = 100, null = True, blank = True)
	name_1 = models.CharField(max_length = 100, null = True, blank = True)
	email_1 = models.CharField(max_length = 100, null = True, blank = True)
	phone_1 = models.CharField(max_length = 100, null = True, blank = True)

	header_2 = models.CharField(max_length = 100, null = True, blank = True)
	name_2 = models.CharField(max_length = 100, null = True, blank = True)
	email_2 = models.CharField(max_length = 100, null = True, blank = True)
	phone_2 = models.CharField(max_length = 100, null = True, blank = True)

	header_3 = models.CharField(max_length = 100, null = True, blank = True)
	name_3 = models.CharField(max_length = 100, null = True, blank = True)
	email_3 = models.CharField(max_length = 100, null = True, blank = True)
	phone_3 = models.CharField(max_length = 100, null = True, blank = True)

	header_4 = models.CharField(max_length = 100, null = True, blank = True)
	name_4 = models.CharField(max_length = 100, null = True, blank = True)
	email_4 = models.CharField(max_length = 100, null = True, blank = True)
	phone_4 = models.CharField(max_length = 100, null = True, blank = True)

	


	def __unicode__(self):
		return 'Help Center'

class Registration(models.Model):
	register_field = models.TextField(max_length = 150, null = True, blank = True)
	login_field = models.TextField(max_length = 150, null = True, blank = True)

	def __unicode__(self):
		return 'Registration'