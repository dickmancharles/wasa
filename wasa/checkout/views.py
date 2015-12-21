from django.conf import settings
from django.shortcuts import render, RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from tenants.models import Tenant, Transaction, Property
from .forms import BillingForm
from tenants.forms import ChargeForm

from .models import PublishableKey, SecretKey

from decimal import *

import datetime
import calendar


# Create your views here.
import stripe
try:
	stripe.api_key = SecretKey.objects.get()
	stripe.api_key = stripe.api_key.secret_key
except:
	stripe.api_key = None



@login_required
def transactions(request):
	charges = Transaction.objects.all()
	context = {
		'charges':charges,
	}
	template = 'transactions.html'
	
	return render(request, template, context)

def group_required(*group_names):
	    def in_groups(u):
	        if u.is_authenticated():
	            if bool(u.groups.filter(name__in=group_names)) | u.is_superuser:
	                return True
	        return False
	    return user_passes_test(in_groups)

@group_required('Tenant')
@login_required()
def dashboard(request):
	user = request.user
	prop = Property.objects.get(tenant=user.tenant)
	rent = user.tenant.rent
	cam = user.tenant.cam
	insurance = user.tenant.insurance

	calc_rent = float(rent+cam+insurance)
	tax = float(request.user.tenant.taxes)

	final_amount = tax + calc_rent


	final_amount  = final_amount * 1.03

	fees = final_amount - (calc_rent+tax)


	# Last payment item
	try:
		lastpayment = Transaction.objects.filter(user=user).order_by('-id')[0]
		amount = lastpayment.amount
		descript = lastpayment.description
		# last payment date
		lastdate = lastpayment.timestamp
		# next payment date
		today = datetime.datetime.now()
		month = today.month
		year = today.year
		nextpayment = month + 1

		if nextpayment == 13:
			nextpayment = 1
		fullmonth = calendar.month_name[nextpayment]

		context = {
			'fees':fees,
			'prop':prop,
			'descript':descript,
			'tax':tax,
			'fullmonth':fullmonth,
			'year':year,
			'lastdate':lastdate,
			'amount':amount,
			'final_amount':final_amount,
			}
	except:
		amount = None
		
		today = datetime.datetime.now()
		month = today.month
		year = today.year
		nextpayment = month + 1

		if nextpayment == 13:
			nextpayment = 1
		fullmonth = calendar.month_name[nextpayment]
		
		context = {
			'fullmonth':fullmonth,
			'year':year,
			'prop':prop,
			'tax':tax,
			'amount':amount,
			'final_amount':final_amount,
		}

	template = 'dashboard.html'
	
	return render(request, template, context)

@login_required
def payment(request):
	try:
		pub_key = PublishableKey.objects.get()
		pub_key = pub_key.publishable_key

	except:
		pub_key = None

	
	
	customer_id = request.user.userstripe.stripe_id
	customer = stripe.Customer.retrieve(customer_id)
	user =  request.user
	  
	# may have conversion issues; note: have not tested corner cases
	comp = request.user.tenant.company
	rent = request.user.tenant.rent
	cam = request.user.tenant.cam
	insurance = request.user.tenant.insurance

	rent_dis = float(rent+cam+insurance)  

	tax = float(request.user.tenant.taxes)


	final_amount = tax + rent_dis

	final_amount  = final_amount * 1.03


	fees = final_amount - (rent_dis+tax)



	
	final_amount = Decimal(final_amount).quantize(Decimal('.000'), rounding=ROUND_HALF_UP).quantize(Decimal('0.01'))
		
	calc_rent =  int(final_amount * 100)


	

	billingform = BillingForm(request.POST or None)
	chargeform = ChargeForm(request.POST or None)
	confirm_message = None
	

	# Charges card
	if request.method == 'POST':
		token = request.POST['stripeToken']
		another = request.POST.get('another', False)
		sub = request.POST.get('subscription', False)
		
		
		if billingform.is_valid():
			name = billingform.cleaned_data['name']
			address_line1 = billingform.cleaned_data['street_address']
			address_city = billingform.cleaned_data['city']
			address_state = billingform.cleaned_data['state']
			address_zip = billingform.cleaned_data['zip_code']		


			try:
				customer = stripe.Customer.retrieve(customer_id)
				card = customer.cards.create(card=token)
				card.name = name
				card.address_line1 = address_line1
				card.address_city = address_city
				card.address_state = address_state
				card.address_zip = address_zip
				card.save()

				if another:
					if chargeform.is_valid():
						amount = chargeform.cleaned_data['amount']
						description = chargeform.cleaned_data['description']
						ref = chargeform.cleaned_data['reference']
						comment = chargeform.cleaned_data['comment']

						another_amount = int(amount*100)

						charge = stripe.Charge.create(
							amount=another_amount, # amount in cents, again
							currency="usd",
							customer = customer,
							description="%s, %s" %(request.user.email,comp)
						)

						if charge:
							# charge event
							r = Transaction(user=user, amount=amount, description=description, reference=ref, comment=comment)
							r.save()

							confirm_message = """
							Thank you for your payment for the amount of %.2f to be applied for %s
							""" %(amount, description)
							billingform = None

				else:
					charge = stripe.Charge.create(
						amount=calc_rent, # amount in cents, again
						currency="usd",
						customer = customer,
						description="%s, %s" %(request.user.email,comp)
					)

					if charge:
						# charge event
						r = Transaction(user=user, amount=final_amount, description="rent", )
						r.save()

						confirm_message = 'Thank you for your payment totalling %.2f' %(final_amount)
						billingform = None

				if sub:
					plan = stripe.Plan.create(
						amount=calc_rent,
						interval='month',
						name=' %s %s Wasa Properties Automated bill payment' 
						%(request.user.tenant.first_Name, request.user.tenant.last_Name ),
						currency='usd',
						id=customer,
					)
					if plan:
						customer.subscriptions.create(plan=customer)
				

			except stripe.CardError, e:
				# The card has been declined
				confirm_message = """
				There was an error in processing your request. 
				Please try again and if the problem continues contact info@wasaproperties.com
				"""
				billingform = None

	context = {
		'fees':fees,
		'final_amount':final_amount,
		'tax':tax,
		'confirm_message':confirm_message,
		'chargeform': chargeform,
		'billingform':billingform,
		'rent_dis':rent_dis,
		'pub_key':pub_key,
	}
	template = 'payment.html'
	
	return render(request, template, context)