from django.db import models

# Create your models here.

class SecretKey(models.Model):
	secret_key = models.CharField(max_length = 32)

	def __unicode__(self):
		return "SecretKey"

class PublishableKey(models.Model):
	publishable_key = models.CharField(max_length = 32)
	
	def __unicode__(self):
		return "PublishableKey"