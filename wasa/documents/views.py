from django.shortcuts import render
from django.conf import settings
from django.core.mail import EmailMessage
from filetransfers.api import serve_file
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import User

# Create your views here.
from contact.forms import ResumeForm
from .models import Resume, Document
from members.models import Position
from pages.models import Career

def group_required(*group_names):
    def in_groups(u):
        if u.is_authenticated():
            if bool(u.groups.filter(name__in=group_names)) | u.is_superuser:
                return True
        return False
    return user_passes_test(in_groups) 


@group_required('Investor')
@login_required()
def investors(request):
	documents = Document.objects.all()
	context = {
			'documents':documents,
		}
	template = 'investor.html'
	return render(request, template, context)

def career(request):
	text = Career.objects.all()
	position = Position.objects.all()
	form = ResumeForm()
	confirm_message = None
	if request.method == 'POST':
		form = ResumeForm(request.POST, request.FILES)

		if form.is_valid():
			# Mail resume
			first_name = form.cleaned_data['first_name']
			last_name = form.cleaned_data['last_name']
			name = first_name + ' ' + last_name
			address = form.cleaned_data['address']
			city = form.cleaned_data['city']
			state = form.cleaned_data['state']
			zipcode = form.cleaned_data['zipcode']
			phone = form.cleaned_data['phone']
			frm = form.cleaned_data['email']
			attach = request.FILES['resume']
			comment = form.cleaned_data['comment']
			
			sbj = 'Resume from %s' %(name)

			msg = """
			\nFrom: %s  \nEmail: %s 
			\nAddress: %s, %s, %s %s

			""" %(name, frm, address, city, state, zipcode)

			# change to wasa.info@crap
			to_us = [settings.EMAIL_HOST_USER]

			email = EmailMessage(sbj, msg, frm, to_us)

			doc = Resume(docfile = request.FILES['resume'], name = name)
			doc.save()

			try:
				email.attach(attach.name, attach.read(), attach.content_type)
				email.send(fail_silently=False)

				form = None
				confirm_message = """
				Thank you for your message. We have received it and will be in touch shortly.
				"""
			except:
				form = None
				confirm_message = """
				There has been an error, please try again. If this problem continues please contact info@wasaproperties.com
				"""
			
			
			
	context = {
		'confirm_message':confirm_message,
		'text':text,
		'position':position,
		'form':form,
	}
	template = 'career.html'
	return render(request, template, context)

@login_required
def document(request):
	documents = Document.objects.all()
	context = {
		'documents':documents,
	}
	template = 'document.html'
	return render(request, template, context)


def download(request, name):
	upload = get_object_or_404(Document, name = name)
	return serve_file(request , upload.docfile)
	
def news(request):
	documents = Document.objects.news()
	context = {
		'documents':documents,
	}
	template = 'news.html'
	return render(request, template, context)


