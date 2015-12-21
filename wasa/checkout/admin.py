from django.contrib import admin
# Register your models here.

from .models import SecretKey, PublishableKey

class PublishableKeyAdmin(admin.ModelAdmin):
	class Meta:
		model = PublishableKey

admin.site.register(PublishableKey, PublishableKeyAdmin)

class SecretKeyAdmin(admin.ModelAdmin):
	class Meta:
		model = SecretKey

admin.site.register(SecretKey, SecretKeyAdmin)