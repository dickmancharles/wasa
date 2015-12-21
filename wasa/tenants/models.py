from django.conf import settings
from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

# Create your models here.
from allauth.account.signals import user_logged_in, user_signed_up
from django.contrib.auth.models import User    
from django.db import models  


import stripe
stripe.api_key = settings.STRIPE_SECRET_KEY



class ChargeQuerySet(models.query.QuerySet):
	def user(self, user):
		return self.filter(user=user)

	def up(self, user):
		return self.get(user=user)


class ChargeManager(models.Manager):
	def get_queryset(self):
		return ChargeQuerySet(self.model, using=self._db)

	def user(self, user):
		return self.get_queryset().user(user)

	def up(self, user):
		return self.get_queryset().up(user)


class Transaction(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, null = True, blank = True)
	timestamp = models.DateTimeField(auto_now_add = True, auto_now = False)
	amount = models.DecimalField(max_digits=10, decimal_places=2)
	description = models.CharField(max_length = 150)
	reference = models.CharField(max_length = 150, null = True, blank = True)
	comment = models.CharField(max_length = 150, null = True, blank = True)

	objects = ChargeManager()
	

	def __unicode__(self):
		return str(self.user) + ' ' + str(self.description)



class Tenant(models.Model): 
	user = models.OneToOneField(settings.AUTH_USER_MODEL, null = True, blank = True)
	first_Name = models.CharField(max_length = 20)
	last_Name = models.CharField(max_length = 20)
	title = models.CharField(max_length = 20)
	company = models.CharField(max_length = 20) # unique=True
	street_address = models.CharField(max_length = 120)
	suite = models.CharField(max_length = 120, null = True, blank = True)
	city = models.CharField(max_length = 12)
	state = models.CharField(max_length = 12)
	zip_code = models.CharField(max_length = 12)
	email = models.EmailField() 
	work_phone = models.CharField(max_length = 12)
	cell_phone =models.CharField(max_length = 12, null = True, blank = True)
	# models.signals.post_save.connect(create_api_key, sender=User)

	# Financials
	rent = models.DecimalField(default = 0, max_digits=10, decimal_places=2, null = True, blank = True)
	taxes = models.DecimalField(default = 0, max_digits=10, decimal_places=2, null = True, blank = True)
	cam = models.DecimalField(default = 0, max_digits=10, decimal_places=2, null = True, blank = True)
	insurance = models.DecimalField(default = 0,max_digits=10, decimal_places=2, null = True, blank = True)

	def __unicode__(self):
		if self.user:
			return str(self.user) + ' ' + str(self.company)
		else:
			return self.company



# properties query and filters
class PropertyQuerySet(models.query.QuerySet):
	def ny(self):
		return self.filter(state ='New York')
		
	def tx(self):
		return self.filter(state ='Texas')
		
	def sc(self):
		return self.filter(state ='South Carolina')

	def nc(self):
		return self.filter(state ='North Carolina')

	def	al(self):
		return self.filter(state ='Alabama')

	def ak(self):
		return self.filter(state ='Alaska')

	def ar(self):
		return self.filter(state ='Arkansas')
	
	def az(self):
		return self.filter(state ='Arizona')

	def ca(self):
		return self.filter(state ='California')
			
	def co(self):
		return self.filter(state ='Colorado')
	
	def ct(self):
		return self.filter(state ='Connecticut')
	
	def de(self):
		return self.filter(state ='Delaware')
	
	def fl(self):
		return self.filter(state ='Florida')
	
	def ga(self):
		return self.filter(state ='Georgia')
	
	def hi(self):
		return self.filter(state ='Hawaii')
	
	def id(self):
		return self.filter(state ='Idaho')
	
	def il(self):
		return self.filter(state ='Illinois')
	
	def indiana(self):
		return self.filter(state ='Indiana')
	
	def ia(self):
		return self.filter(state ='Iowa')
	
	def ks(self):
		return self.filter(state ='Kansas')
	
	def ky(self):
		return self.filter(state ='Kentucky')
	
	def la(self):
		return self.filter(state ='Louisiana')
	
	def me(self):
		return self.filter(state ='Maine')
	
	def md(self):
		return self.filter(state ='Maryland')
	
	def ma(self):
		return self.filter(state ='Massachusetts')
	
	def mi(self):
		return self.filter(state ='Michigan')
	
	def mn(self):
		return self.filter(state ='Minnesota')

	def ms(self):
		return self.filter(state ='Mississippi')
	
	def mo(self):
		return self.filter(state ='Missouri')
	
	def mt(self):
		return self.filter(state ='Montana')
	
	def ne(self):
		return self.filter(state ='Nebraska')
	
	def nh(self):
		return self.filter(state ='New Hampshire')
	
	def nv(self):
		return self.filter(state ='Nevada')
	
	def nj(self):
		return self.filter(state ='New Jersey')
	
	def nd(self):
		return self.filter(state ='North Dakota')
	
	def oh(self):
		return self.filter(state ='Ohio')
	
	def ok(self):
		return self.filter(state ='Oklahoma')
	
	def oreg(self):
		return self.filter(state ='Oregon')
	
	def pa(self):
		return self.filter(state ='Pennsylvania')
	
	def ri(self):
		return self.filter(state ='Road Island')
	
	def sd(self):
		return self.filter(state ='South Dakota')

	def tn(self):
		return self.filter(state ='Tennessee')

	def ut(self):
		return self.filter(state ='Utah')
	
	def vt(self):
		return self.filter(state ='Vermont')
	
	def va(self):
		return self.filter(state ='Virginia')
	
	def dc(self):
		return self.filter(state ='Washington DC')
	
	def wa(self):
		return self.filter(state ='Washington')
	
	def wv(self):
		return self.filter(state ='West Virginia')
	
	def wi(self):
		return self.filter(state ='Wisconsin')
	
	def wy(self):
		return self.filter(state ='Wyoming')

	def nm(self):
		return self.filter(state ='New Mexico')
	

class PropManager(models.Manager):
	def get_queryset(self):
		return PropertyQuerySet(self.model, using=self._db)

	def ny(self):
		return self.get_queryset().ny()

	def tx(self):
		return self.get_queryset().tx()

	def sc(self):
		return self.get_queryset().sc()

	def nc(self):
		return self.get_queryset().nc()

	def	al(self):
		return self.get_queryset().al()

	def ak(self):
		return self.get_queryset().ak()

	def ar(self):
		return self.get_queryset().ar()
	
	def az(self):
		return self.get_queryset().az()

	def ca(self):
		return self.get_queryset().ca()
			
	def co(self):
		return self.get_queryset().co()
	
	def ct(self):
		return self.get_queryset().ct()
	
	def de(self):
		return self.get_queryset().de()
	
	def fl(self):
		return self.get_queryset().fl()
	
	def ga(self):
		return self.get_queryset().ga()
	
	def hi(self):
		return self.get_queryset().hi()
	
	def id(self):
		return self.get_queryset().id()
	
	def il(self):
		return self.get_queryset().il()
	
	def indiana(self):
		return self.get_queryset().indiana()
	
	def ia(self):
		return self.get_queryset().ia()
	
	def ks(self):
		return self.get_queryset().ks()
	
	def ky(self):
		return self.get_queryset().ky()
	
	def la(self):
		return self.get_queryset().la()
	
	def me(self):
		return self.get_queryset().me()
	
	def md(self):
		return self.get_queryset().md()
	
	def ma(self):
		return self.get_queryset().ma()
	
	def mi(self):
		return self.get_queryset().mi()
	
	def mn(self):
		return self.get_queryset().mn()

	def ms(self):
		return self.get_queryset().ms()
	
	def mo(self):
		return self.get_queryset().mo()
	
	def mt(self):
		return self.get_queryset().mt()
	
	def ne(self):
		return self.get_queryset().ne()
	
	def nv(self):
		return self.get_queryset().nv()
	
	def nj(self):
		return self.get_queryset().nj()
	
	def nh(self):
		return self.get_queryset().nh()
	
	def nd(self):
		return self.get_queryset().nd()
	
	def oh(self):
		return self.get_queryset().oh()
	
	def ok(self):
		return self.get_queryset().ok()
	
	def oreg(self):
		return self.get_queryset().oreg()
	
	def pa(self):
		return self.get_queryset().pa()
	
	def ri(self):
		return self.get_queryset().ri()
	
	def sd(self):
		return self.get_queryset().sd()

	def tn(self):
		return self.get_queryset().tn()

	def ut(self):
		return self.get_queryset().ut()
	
	def vt(self):
		return self.get_queryset().vt()
	
	def va(self):
		return self.get_queryset().va()
	
	def dc(self):
		return self.get_queryset().dc()
	
	def wa(self):
		return self.get_queryset().wa()
	
	def wv(self):
		return self.get_queryset().wv()
	
	def wi(self):
		return self.get_queryset().wi()
	
	def wy(self):
		return self.get_queryset().wy()

	def nm(self):
		return self.get_queryset().nm()

# Dept cat
PROP_CATEGORIES = (
	('Alabama','Alabama'), 
	('Alaska', 'Alaska'),
	('Arizona','Arizona'), 
	('Arkansas','Arkansas'), 
	('California','California'), 
	('Colorado', 'Colorado'), 
	('Connecticut','Connecticut'), 
	('Delaware','Delaware'), 
	('Florida','Florida'), 
	('Georgia','Georgia'), 
	('Hawaii','Hawaii'), 
	('Idaho','Idaho'), 
	('Illinois','Illinois'), 
	('Indiana','Indiana'), 
	('Iowa','Iowa'), 
	('Kansas','Kansas'), 
	('Kentucky','Kentucky'), 
	('Louisiana','Louisiana'), 
	('Maine','Maine'), 
	('Maryland','Maryland'), 
	('Massachusetts','Massachusetts'), 
	('Michigan','Michigan'), 
	('Minnesota','Minnesota'), 
	('Mississippi','Mississippi'), 
	('Missouri','Missouri'), 
	('Montana','Montana'), 
	('Nebraska','Nebraska'), 
	('Nevada','Nevada'), 
	('New Hampshire','New Hampshire'), 
	('New Jersey','New Jersey'), 
	('New Mexico','New Mexico'), 
	('New York', 'New York'),
	('North Carolina', 'North Carolina'),
	('North Dakota','North Dakota'), 
	('Ohio','Ohio'), 
	('Oklahoma','Oklahoma'), 
	('Oregon','Oregon'), 
	('Pennsylvania','Pennsylvania'), 
	('Rhode Island','Rhode Island'), 
	('South Carolina', 'South Carolina'),
	('South Dakota','South Dakota'), 
	('Tennessee','Tennessee'), 
	('Texas', 'Texas'),
	('Utah','Utah'), 
	('Vermont','Vermont'), 
	('Virginia','Virginia'), 
	('Washington','Washington'),
	('Washington DC','Washington DC'), 
	('West Virginia','West Virginia'), 
	('Wisconsin','Wisconsin'), 
	('Wyoming','Wyoming'),

)

class Property(models.Model): 
	tenant = models.ManyToManyField(Tenant, null = True, blank = True)
	name = models.CharField(max_length = 150)# unique = True
	description = models.TextField(max_length = 1500, null = True, blank = True)
	street_address = models.CharField(max_length = 120)
	apt = models.CharField(max_length = 120, null = True, blank = True)
	city = models.CharField(max_length = 12)
	state = models.CharField(max_length = 120, choices = PROP_CATEGORIES, default = '')
	zip_code = models.CharField(max_length = 12)
	slug = models.SlugField(unique = True)
	objects = PropManager()
	
	# Demographics # Might be better to change to string 
	pop1m = models.IntegerField(default = 0, null = True, blank = True)
	pop3m = models.IntegerField(default = 0, null = True, blank = True)
	pop5m = models.IntegerField(default = 0, null = True, blank = True)
	house1m = models.IntegerField(default = 0, null = True, blank = True)
	house3m = models.IntegerField(default = 0, null = True, blank = True)
	house5m = models.IntegerField(default = 0, null = True, blank = True)
	income1m = models.IntegerField(default = 0, null = True, blank = True)
	income3m = models.IntegerField(default = 0, null = True, blank = True)
	income5m = models.IntegerField(default = 0, null = True, blank = True)

	# Metrics
	total_sqft = models.CharField(max_length = 150, null = True, blank = True)
	occupancy = models.CharField(max_length = 150, null = True, blank = True)

	# traffic
	road1name = models.CharField(max_length = 150, null = True, blank = True)
	road1numbers = models.CharField(max_length = 150, null = True, blank = True)
	road2name = models.CharField(max_length = 150, null = True, blank = True)
	road2numbers = models.CharField(max_length = 150, null = True, blank = True)

	
	

	def __unicode__(self):
		return self.name

	class Meta:
		unique_together = ('name', 'slug')

	def get_absolute_url(self):
		return reverse("singleprop", kwargs = {"slug": self.slug,})

class Suite(models.Model):
	location = models.ForeignKey(Property)
	featured = models.BooleanField(default=False)
	tenant = models.CharField(max_length = 50, null = True, blank = True)
	suite = models.CharField(max_length = 10, null = True, blank = True)
	sqft = models.CharField(max_length = 10, null = True, blank = True)

	def __unicode__(self):
		if self.featured:
			return str(self.location) + ' ' + 'featured'
		else:
			return str(self.location)


class PropImage(models.Model):
	prop = models.ForeignKey(Property)
	image = models.ImageField(upload_to= 'members/')
	featured = models.BooleanField(default=False)
	sitemap = models.BooleanField(default=False)

	def __unicode__(self):
		if self.featured:
			return str(self.prop.name) + ' ' + 'featured'

		elif self.sitemap:
			return str(self.prop.name) + ' ' + 'sitemap'
		else:
			return str(self.prop.name)
	
		
# # stores users info to submit into stripe 
# class UserStripe(models.Model):
# 	user = models.OneToOneField(settings.AUTH_USER_MODEL)
# 	stripe_id = models.CharField(max_length = 200, null = True, blank = True)
	
# 	def __unicode__(self):
# 		return str(self.user)

# # creates UserStripe when user logs in for the first time
# def stripe_callback(sender, request, user, **kwargs):
# 	user_stripe_account, created = UserStripe.objects.get_or_create(user=user)
# 	if user_stripe_account.stripe_id is None or user_stripe_account.stripe_id == '':
# 		new_stripe_id = stripe.Customer.create(email=user.email)
# 		user_stripe_account.stripe_id = new_stripe_id['id']
# 		user_stripe_account.save()

# user_logged_in.connect(stripe_callback)
