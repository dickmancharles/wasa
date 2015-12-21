from django import forms
from tenants.models import Property 

class RepairForm(forms.Form):
	name = forms.CharField(max_length = 120, required = True)
	phone = forms.CharField(max_length = 200, required = False)
	location = forms.CharField(max_length = 200, required = True)
	message = forms.CharField(widget = forms.Textarea, required=True)

class ContactForm(forms.Form):
	name = forms.CharField(max_length = 120, required = True)
	subject = forms.CharField(max_length = 200, required = True)
	email = forms.EmailField(required = True)
	phone = forms.CharField(max_length=15, required = True)
	message = forms.CharField(widget = forms.Textarea, required = True)

class ResumeForm(forms.Form):
	first_name = forms.CharField(label='First Name', max_length = 120, required = True)
	last_name = forms.CharField(label='Last Name', max_length = 15, required = True)
	address = forms.CharField(max_length = 200, required = True)
	city = forms.CharField(max_length = 20, required = True)
	state = forms.CharField(max_length = 20, required = True)
	zipcode = forms.CharField(label='Zip Code', max_length = 7, required = True)
	phone = forms.IntegerField(required = True)
	email = forms.EmailField(required = True)
	resume = forms.FileField(label='Attach a Resume', required = True)
	comment = forms.CharField(label='Add a Cover letter', widget = forms.Textarea, required = True)


class SalesForm(forms.Form):
	date = forms.CharField(label = 'Date:D/M/Y', max_length = 120, required = True)
	business = forms.CharField(max_length = 120, required = True)
	location = forms.CharField(label = 'Property Name', max_length = 120, required = True)
	address = forms.CharField(label = 'Property Address',max_length = 120, required = True)
	email = forms.EmailField(required = True)
	phone = forms.CharField(max_length = 15, required = False)
	sales_year = forms.CharField(label = 'Sales Year', max_length = 120, required = True)
	sales_amount = forms.CharField(label = 'Sales Amount', max_length = 120, required = True)
	
	comments = forms.CharField(widget = forms.Textarea, required = False)
	
	