from django import forms

class BillingForm(forms.Form):
	name = forms.CharField(max_length = 120, required = True)
	street_address = forms.CharField(max_length = 200, required = True)
	suite = forms.CharField(max_length = 200, required = False)
	city = forms.CharField(max_length = 20, required = True)
	state = forms.CharField(max_length = 20, required = True)
	zip_code = forms.CharField(max_length = 5, required = True)
