from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render
from django.shortcuts import render, render_to_response, RequestContext
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
import json

# Create your views here.
from documents.models import Document
from .forms import RegForm
from .models import Tenant, Property, PropImage, Suite
from pages.models import CompanyProfile, OwnersRep, AcquisitionPage, Registration, HelpCenter
import urllib2
import requests


def helpcenter(request):
	text = HelpCenter.objects.all()
	context = {
		'text':text,
	}
	
	template = 'helpcenter.html'
	
	return render(request, template, context)

def myaccount(request):
	context = locals()
	template = 'myaccount.html'
	
	return render(request, template, context)




def singleprop(request, slug):
	prop = Property.objects.get(slug = slug)
	images = PropImage.objects.filter(prop = prop)
	documents = Document.objects.filter(prop = prop)
	suite = Suite.objects.filter(location = prop)

 	context = {
 		'suite': suite,
 		'documents': documents,
 		'prop': prop,
 		'images': images,
 	}	
	template = 'prop/singleprop.html'
	
	return render(request, template, context)

@login_required()
def prop(request):
	
	ny = Property.objects.ny()
	tx = Property.objects.tx()
	sc = Property.objects.sc()
	nc = Property.objects.nc()
	al = Property.objects.al()
	ak = Property.objects.ak()
	ar = Property.objects.ar()
	az = Property.objects.az()
	ca = Property.objects.ca()
	co = Property.objects.co()
	ct = Property.objects.ct()
	de = Property.objects.de()
	dc = Property.objects.dc()
	fl = Property.objects.fl()
	ga = Property.objects.ga()
	hi = Property.objects.hi()
	idaho = Property.objects.id()
	il = Property.objects.il()
	indiana = Property.objects.indiana()
	ia = Property.objects.ia()
	ks = Property.objects.ks()
	ky = Property.objects.ky()
	la = Property.objects.la()
	me = Property.objects.me()
	md = Property.objects.md()
	ma = Property.objects.ma()
	mi = Property.objects.mi()
	mn = Property.objects.mn()
	ms = Property.objects.ms()
	mo = Property.objects.mo()
	mt = Property.objects.mt()
	ne = Property.objects.ne()
	nv = Property.objects.nv()
	nj = Property.objects.nj()
	nh = Property.objects.nh()
	nd = Property.objects.nd()
	oh = Property.objects.oh()
	ok = Property.objects.ok()
	oreg = Property.objects.oreg()
	pa = Property.objects.pa()
	ri = Property.objects.ri()
	sd = Property.objects.sd()
	tn = Property.objects.tn()
	ut = Property.objects.ut()
	vt = Property.objects.vt()
	va = Property.objects.va()
	wa = Property.objects.wa()
	wv = Property.objects.wv()
	wi = Property.objects.wi()
	wy = Property.objects.wy()
	nm = Property.objects.nm()

	context = {
		'nm':nm,
		'ny':ny,
		'tx':tx,
		'sc':sc,
		'nc':nc,
		'al':al,
		'ak':ak,	
		'ar':ar,
		'az':az,
		'ca':ca,
		'co':co,
		'ct':ct,
		'de':de,
		'dc':dc,
		'fl':fl,
		'ga':ga,
		'hi':hi,
		'idaho':idaho,
		'il':il,
		'indiana':indiana,
		'ia':ia,
		'ks':ks,
		'ky':ky,
		'la':la,
		'me':me,
		'md':md,
		'ma':ma,
		'mi':mi,
		'mn':mn,
		'ms':ms,
		'mo':mo,
		'mt':mt,
		'ne':ne,
		'nv':nv,
		'nj':nj,
		'nh':nh,
		'nd':nd,
		'oh':oh,
		'ok':ok,
		'oreg':oreg,
		'pa':pa,
		'ri':ri,
		'sd':sd,
		'tn':tn,
		'ut':ut,
		'vt':vt, 
		'va':va,
		'wa':wa,
		'wv':wv,
		'wi':wi,
		'wy':wy,
	}

	template = 'properties.html'
	
	return render(request, template, context)

def login(request):
	context = locals()
	template = 'login.html'
	
	return render(request, template, context)


def acquisitions(request):
	text = AcquisitionPage.objects.all()
	context = {
		'text':text,
	}
	template = 'acquisitions.html'
	
	return render(request, template, context)

def owners(request):
	try:
	 	doc =  Document.objects.get(brochure = True)
	except Exception, e:
	 	doc = None
	
	text = OwnersRep.objects.all() 
	
	context = {
		'text':text,
		'doc':doc,
	}
	template = 'owners.html'
	
	return render(request, template, context)


def team(request):
	context = locals()
	template = 'team.html'
	
	return render(request, template, context)

def companyprofile(request):
	text = CompanyProfile.objects.all()
	context = {
		'text':text,
	}
	template = 'cprofile.html'
	
	return render(request, template, context)
	

def home(request):
	context = locals()
	template = 'home.html'
	
	return render(request, template, context)

def register(request):
	form = RegForm(request.POST or None)
	text = Registration.objects.all()

	title = "Registration Form"
	confirm = None
	context = {
		'text': text,
		'title': title,
		'form': form,
		'confirm': confirm,
	}
	
	if form.is_valid():
		# save form for tenant
		tenants = form
		tenants.save()

		# emails form 
		# Varible data to link clean info 
		name = form.cleaned_data['first_Name'] + ' ' + form.cleaned_data['last_Name']
		address = form.cleaned_data['street_address'] + ' Suite: ' + form.cleaned_data['suite'] + '\n' + form.cleaned_data['city'] + ' ' + form.cleaned_data['state'] + ', ' + form.cleaned_data['zip_code']
		company = form.cleaned_data['company'] 
		email = form.cleaned_data['email']
		phone = form.cleaned_data['work_phone']
		title = form.cleaned_data['title']


		# Links data to varibles 
		subject = 'New registeration by, %s' %(name)
		
		msg = "%s, %s of %s. Has just registered. \nTheir contact information is: \nEmail: %s \nPhone: %s \nAddress: %s "%(name, title, company, email, phone, address)
		
		frm = email
		to_us = [settings.EMAIL_RECEIVE]

		send_mail(subject, msg, frm, to_us, fail_silently=False) 

		# print to_us #Can store info in model 
		


		confirm = """
		Thank you! You will soon have access to Wasa Properties Online Portal. \n Please allow 72 hours 
		to process your information. You will receive confirmation email once you're granted an access to 
		the portal. If you have any questions or concerns, 
		please send us an email to info@wasaproperties.com.
		"""
		text = None
		form = None
		title = None
		context = {
			'text':text,
			'confirm':confirm,
			'form': form,
			'title': title,
		}

	template = 'register.html'

	return render(request, template, context)