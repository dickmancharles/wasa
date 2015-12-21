from django import forms
from .models import Tenant, Transaction

class RegForm(forms.ModelForm):
	suite = forms.CharField(label = "Suite Number")
	street_address = forms.CharField(label = "Street Address")
	work_phone = forms.CharField(label = "Work Phone")
	cell_phone = forms.CharField(label = "Cell Phone", required = False)
	zip_code = forms.CharField(label = "Zip Code")
	class Meta:
		model = Tenant
		fields = '__all__'
		exclude = ('user','rent','cam','insurance','rent','taxes')


class ChargeForm(forms.ModelForm):
	class Meta:
		model = Transaction
		fields = '__all__'
		exclude = ('user',)

