from django.contrib import admin

# Register your models here.
# UserStripe
from .models import Tenant, Property, Transaction, Suite

class TenantAdmin(admin.ModelAdmin):
	class Meta:
		model = Tenant

admin.site.register(Tenant, TenantAdmin)
		
# class UserStripeAdmin(admin.ModelAdmin):
# 	class Meta:
# 		model = UserStripe

# admin.site.register(UserStripe, UserStripeAdmin)


class PropertyAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('name',)}
	class Meta:
		model = Property

admin.site.register(Property, PropertyAdmin)


class TransactionAdmin(admin.ModelAdmin):
	class Meta:
		model = Transaction

admin.site.register(Transaction, TransactionAdmin)

class SuiteAdmin(admin.ModelAdmin):
	class Meta:
		model = Suite

admin.site.register(Suite, SuiteAdmin)

