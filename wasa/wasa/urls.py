from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

# from tastypie.api import Api
# from tenants.api.resources import TenantResource

# v1_api = Api(api_name='v1')
# v1_api.register(TenantResource())


urlpatterns = patterns('',

    # url(r'dashboard/', 'checkout.views.dashboard', name='dashboard'),
    # url(r'payment/', 'checkout.views.payment', name='payment'),
    # url(r'transactions/', 'checkout.views.transactions', name='transactions'),
    url(r'^register/$', 'tenants.views.register', name='register'),
    url(r"^login/$", 'tenants.views.login', name='login'),
    url(r'company-profile/', 'tenants.views.companyprofile', name='companyprofile'),
    url(r'^team/$', 'members.views.team', name='team'),
    url(r'repair/', 'contact.views.repair', name='repair'),
    url(r'^prop/$', 'tenants.views.prop', name='properties'),
    url(r'^prop/(?P<slug>[\w-]+)/$', 'tenants.views.singleprop', name='singleprop'),
    url(r'acquisitions/', 'tenants.views.acquisitions', name='acquisitions'),
    # url(r'myaccount/', 'tenants.views.myaccount', name='myaccount'),
    # url(r'salesreport/', 'contact.views.sales', name='salesreport'),
    url(r'contact/', 'contact.views.contact', name='contact'),
    url(r'^career/$', 'documents.views.career', name='career'),
    url(r'^helpcenter/$', 'tenants.views.helpcenter', name='helpcenter'),
     url(r'^investors/$', 'documents.views.investors', name='investors'),
    url(r'^news/$', 'documents.views.news', name='news'),
    # url(r'^doccenter/$', 'documents.views.document', name='document'),
    url(r'^media/documents/(?P<name>.+)/$', 'documents.views.download', name='download'),
    url(r'^$', 'tenants.views.home', name='home'),
    url(r'owners/', 'tenants.views.owners', name='owners'),
    url(r'^admin/', include(admin.site.urls)),
    (r'^accounts/', include('allauth.urls')),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.MEDIA_ROOT}),
    # url(r'^api/', include(v1_api.urls)),
  
)
admin.site.site_header = 'Wasa Properties'