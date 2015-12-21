"""
    Django settings for wasa project.
    
    For more information on this file, see
    https://docs.djangoproject.com/en/1.7/topics/settings/
    
    For the full list of settings and their values, see
    https://docs.djangoproject.com/en/1.7/ref/settings/
    """

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Register your models here.

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = ''
EMAIL_RECEIVE = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_PORT = 587
EMAIL_USE_TLS = True


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '!tx3!^)xss#f5od*1hp5o)onkebm+)*%gkvonv04h%hbz=_o1d'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = (
                  'django.contrib.humanize',
                  'django.contrib.admin',
                  'django.contrib.auth',
                  'django.contrib.contenttypes',
                  'django.contrib.sites',
                  'django.contrib.sessions',
                  'django.contrib.messages',
                  'django.contrib.staticfiles',
                  'allauth',
                  'allauth.account',
                  'crispy_forms',
                  'tenants',
                  'stripe',
                  'members',
                  'documents',
                  'filetransfers',
                  'pages',
                  'checkout',
                  
                  )


SITE_ID = 1

LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/'
ACCOUNT_ADAPTER = 'tenants.adapter.MyAccountAdapter'
ACCOUNT_AUTHENTICATION_METHOD = "username_email" #(="username" | "email" | "username_email" )
ACCOUNT_CONFIRM_EMAIL_ON_GET = True
ACCOUNT_EMAIL_CONFIRMATION_ANONYMOUS_REDIRECT_URL = LOGIN_URL
ACCOUNT_EMAIL_CONFIRMATION_AUTHENTICATED_REDIRECT_URL = LOGIN_REDIRECT_URL
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 9
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = 'None' # options "mandatory", "optional", None
ACCOUNT_EMAIL_SUBJECT_PREFIX = "Subject: "
ACCOUNT_DEFAULT_HTTP_PROTOCOL = "https"
ACCOUNT_LOGOUT_ON_GET = True
ACCOUNT_LOGOUT_REDIRECT_URL = "/register/"
ACCOUNT_SIGNUP_FORM_CLASS = 'tenants.forms.RegForm'
ACCOUNT_SIGNUP_PASSWORD_VERIFICATION =True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USER_MODEL_USERNAME_FIELD = "username"
ACCOUNT_USER_MODEL_EMAIL_FIELD = "email"
# ACCOUNT_USER_DISPLAY (=a callable returning user.username)
ACCOUNT_USERNAME_MIN_LENGTH = 4
# ACCOUNT_USERNAME_BLACKLIST (=[])
ACCOUNT_USERNAME_REQUIRED = True
ACCOUNT_PASSWORD_INPUT_RENDER_VALUE = False
ACCOUNT_PASSWORD_MIN_LENGTH = 6
ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = True
# AUTH_USER_MODEL = 'tenants.Profile'
USE_XSENDFILE = True


CRISPY_TEMPLATE_PACK = 'bootstrap3'

# Stripe Info
# Test Key
STRIPE_PUBLISHABLE_KEY = ''
STRIPE_SECRET_KEY = ''

# Live key
STRIPE_PUBLISHABLE_KEY = ''
STRIPE_SECRET_KEY = ''



MIDDLEWARE_CLASSES = (
                      'django.contrib.sessions.middleware.SessionMiddleware',
                      'django.middleware.common.CommonMiddleware',
                      'django.middleware.csrf.CsrfViewMiddleware',
                      'django.contrib.auth.middleware.AuthenticationMiddleware',
                      'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
                      'django.contrib.messages.middleware.MessageMiddleware',
                      'django.middleware.clickjacking.XFrameOptionsMiddleware',
                      )

ROOT_URLCONF = 'wasa.urls'

WSGI_APPLICATION = 'wasa.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'sqlite3',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/New_York'

USE_I18N = True

USE_L10N = True

USE_TZ = True

TEMPLATE_CONTEXT_PROCESSORS = (
             "django.contrib.auth.context_processors.auth",
             "django.core.context_processors.debug",
             "django.core.context_processors.request",
             "django.core.context_processors.i18n",
             "django.core.context_processors.media",
             "django.core.context_processors.static",
             "django.core.context_processors.tz",
             "django.core.context_processors.request",
             "django.core.context_processors.csrf",
             "django.contrib.messages.context_processors.messages",
             "allauth.account.context_processors.account",
             "allauth.socialaccount.context_processors.socialaccount",
             )

AUTHENTICATION_BACKENDS = (
       # Needed to login by username in Django admin, regardless of `allauth`
       "django.contrib.auth.backends.ModelBackend",
       
       # `allauth` specific authentication methods, such as login by e-mail
       "allauth.account.auth_backends.AuthenticationBackend",
       )

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/




STATIC_URL = '/static/'
STATIC_ROOT = '/Users/hanadickman/Desktop/wasa-dev/static/'

MEDIA_ROOT = '/Users/hanadickman/Desktop/wasa-dev/static/media/'
MEDIA_URL = '/media/'

STATICFILES_DIRS = (
      '/Users/hanadickman/Desktop/wasa-dev/static/static/',

    )

TEMPLATE_DIRS = (
     '/Users/hanadickman/Desktop/wasa-dev/static/templates/',

                 )
