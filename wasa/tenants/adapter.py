from django.conf import settings
from django.contrib.auth.models import Group
from allauth.account.adapter import DefaultAccountAdapter

class MyAccountAdapter(DefaultAccountAdapter):

	def get_login_redirect_url(self, request):
	
		if request.user.groups.filter(name='Tenant').exists():
			path = "/accounts/login/dashboard/"
		elif request.user.groups.filter(name='Investor').exists():
			path = "/investors/"
		else:
			path = '/prop/'

		return path

	def get_logout_redirect_url(self, request):
		if request.user.groups.filter(name='Tenant').exists() or request.user.is_staff:
			path = "/register/"
		elif request.user.groups.filter(name='Investor').exists():
			path = "/investors/"
		else:
			path = '/'

		return path