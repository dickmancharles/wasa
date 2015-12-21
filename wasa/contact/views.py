from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render

# Create your views here.
from .forms import ContactForm, SalesForm, RepairForm

def repair(request):
	form = RepairForm(request.POST or None)
	title = "Repair Request"
	confirm_message = None
	email = request.user.email

	if form.is_valid():
		name = form.cleaned_data['name']
		message = form.cleaned_data['message']
		frm = email
		location = form.cleaned_data['location']

		sbj = 'Repair Request from: %s, %s.' %(name, frm)

		msg = '\nFrom: %s \nEmail: %s \nLocation: %s\nMessage: \n%s ' %(name, frm, location, message)

		# change to info@wasa.com
		to_us = [settings.EMAIL_RECEIVE]
	
		send_mail(sbj, msg, frm, to_us, fail_silently=False) 

		title = None
		form = None
		confirm_message = """
		Thank you for your submission. We will review it and contact you if any additional information is needed.
		"""
		
	context = {
		'title': title,
		'form': form,
		'confirm_message':confirm_message,	
	}
	
	template = 'repair.html'
	
	return render(request, template, context)

def sales(request):
	form = SalesForm(request.POST or None)
	title = "Contact Us"
	confirm_message = None

	if form.is_valid():
		name = form.cleaned_data['business']
		message = form.cleaned_data['comments']
		email = form.cleaned_data['email']
		phone = form.cleaned_data['phone']
		sales_year = form.cleaned_data['sales_year']
		address = form.cleaned_data['address']
		sales_amount = form.cleaned_data['sales_amount']
		frm = form.cleaned_data['email']
	

		sbj = 'From: %s, %s. Sales Report for the year of: %s.' %(name, frm, sales_year)

		msg = """
		\nFrom: %s \nEmail: %s  \nSales Report for %s, located at %s, for the year of %s. 
		\nAmount of sales $%s.
		\nAdditional Commeents:
		\n%s
		""" %(name, email, name, address, sales_year, sales_amount, message)
		# change to info@wasa.com
		to_us = [settings.EMAIL_RECEIVE]
	
		send_mail(sbj, msg, frm, to_us, fail_silently=False) 

		title = None
		form = None
		confirm_message = """
		Thank you for your submission. We will review it and contact you if any additional information is needed.
		"""
		
	context = {
		'title': title,
		'form': form,
		'confirm_message':confirm_message,	
	}
	
	template = 'salesreport.html'
	
	return render(request, template, context)

def contact(request):
	form = ContactForm(request.POST or None)
	title = "Contact Us"
	confirm_message = None

	if form.is_valid():
		name = form.cleaned_data['name']
		message = form.cleaned_data['message']
		email = form.cleaned_data['email']
		phone = form.cleaned_data['phone']
		frm = form.cleaned_data['email']

		sbj = 'Contact Us. From: %s, %s. Subject: %s' %(name, frm, form.cleaned_data['subject'])
		msg = 'From: %s \nEmail: %s \nPhone: %s \nMessage: %s ' %(name, email, phone, message)

		# change to info@wasa.com
		to_us = [settings.EMAIL_RECEIVE]
	
		send_mail(sbj, msg, frm, to_us, fail_silently=False) 

		title = None
		form = None
		confirm_message = """
		Thank you for your message. We have received it and will be in touch shortly.
		"""
		
	context = {
		'title': title,
		'form': form,
		'confirm_message':confirm_message,	
	}

	template = 'contact.html'
	
	return render(request, template, context)
