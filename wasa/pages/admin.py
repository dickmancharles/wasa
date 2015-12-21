from django.contrib import admin

# Register your models here.
from .models import OwnersRep, CompanyProfile, AcquisitionPage, Career, Registration, HelpCenter


class HelpCenterAdmin(admin.ModelAdmin):
	class Meta:
		model = HelpCenter

admin.site.register(HelpCenter, HelpCenterAdmin)

class OwnersRepAdmin(admin.ModelAdmin):
	class Meta:
		model = OwnersRep

admin.site.register(OwnersRep, OwnersRepAdmin)
		
class CompanyProfileAdmin(admin.ModelAdmin):
	class Meta:
		model = CompanyProfile

admin.site.register(CompanyProfile, CompanyProfileAdmin)

class AcquisitionAdmin(admin.ModelAdmin):
	class Meta:
		model = AcquisitionPage

admin.site.register(AcquisitionPage, AcquisitionAdmin)

class CareerAdmin(admin.ModelAdmin):
	class Meta:
		model = Career

admin.site.register(Career, CareerAdmin)

class RegistrationAdmin(admin.ModelAdmin):
	class Meta:
		model = Registration

admin.site.register(Registration, RegistrationAdmin)