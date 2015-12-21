from django.shortcuts import render
from django.shortcuts import render, render_to_response, RequestContext
from django.contrib.auth.models import User


# Create your views here.
from .models import StaffMember, StaffMemberImage

def team(request):
	principals = StaffMember.objects.prin()
	executives = StaffMember.objects.executive()
	
	

	context = {
		'principals':principals,
		'executives':executives,
	}
	template = 'team.html'
	
	return render(request, template, context)



