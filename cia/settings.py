"""
Django settings for cia project.

Generated by 'django-admin startproject' using Django 2.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '#s6=@c-7v412-p6nxp17a@p^%rau--v=t&vd!7dh(sl&f4a4p%'

# SECURITY WARNING: don't run with debug turned on in production!
#DEBUG = True
DEBUG = True
#SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False
SECURE_BROWSER_XSS_FILTER = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True


#ALLOWED_HOSTS = ['167.71.238.192','cia.atria.edu','test.ciadev.ninja','iot.atria.edu']
ALLOWED_HOSTS = ['test.ciadev.ninja','sufibox']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'phonenumber_field',
    'api',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'rest_auth.registration',
        'django_rest_passwordreset',
    'corsheaders',
    'rest_framework',
    'rest_framework.authtoken',  # <-- Here
    'rest_auth',
    'widget_tweaks',
    'crispy_forms',
    'phone_field',
]

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


SITE_ID = 1
AUTH_USER_MODEL = 'api.User'
CRISPY_TEMPLATE_PACK = 'bootstrap4'
PHONENUMBER_DB_FORMAT = 'E164'
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
     'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'cia.urls'

CORS_ORIGIN_ALLOW_ALL =True
CORS_ALLOW_CREDENTIALS =True

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'cia.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

'''
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
'''
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'cia',
        'USER': 'cia',
        'PASSWORD': 'ciafriday',
        'HOST': 'localhost',
        'PORT': '',
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
AUTHENTICATION_BACKENDS = (
   # ('django.contrib.auth.backends.ModelBackend'),
    ('django.contrib.auth.backends.AllowAllUsersModelBackend'),
  #  ('api.models.EmailOrUsernameModelBackend'),
     # `allauth` specific authentication methods, such as login by e-mail
 ("allauth.account.auth_backends.AuthenticationBackend"),
)



STATIC_ROOT = os.path.join(BASE_DIR, 'static')


ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_REQUIRED = True   
ACCOUNT_USERNAME_REQUIRED = False


#ACCOUNT_EMAIL_VERIFICATION="none"
# for rest auth registeration
REST_AUTH_SERIALIZERS = {
    #"USER_DETAILS_SERIALIZER": "api.serializers.CustomUserDetailsSerializer",
   # "USER_DETAILS_SERIALIZER": "api.serializers.UserSerializer",
    "USER_DETAILS_SERIALIZER": "api.serializers.CustomUserDetailsSerializer",
    #"LOGIN_SERIALIZER":"api.serializers.CustomLoginSerializer",
    #'PASSWORD_RESET_SERIALIZER': 
     #   "api.serializers.PasswordResetSerializer",
    
}
REST_AUTH_REGISTER_SERIALIZERS = {
    "REGISTER_SERIALIZER": "api.serializers.NewRegisterSerializer",
    #"REGISTER_SERIALIZER": "api.serializers.RegisterSerializerCustom",
}


REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ]
}


'''
REST_AUTH_LOGIN_SERIALIZERS = {
    "LOGIN_SERIALIZER":"api.serializers.CustomLoginSerializer",
}

REST_AUTH_SERIALIZERS = {
    'LOGIN_SERIALIZER': 'path.to.custom.LoginSerializer',
    'TOKEN_SERIALIZER': 'path.to.custom.TokenSerializer',
    ...
}'''

ACCOUNT_ADAPTER = 'api.adapters.CustomUserAccountAdapter'

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'communities.atria@gmail.com'
EMAIL_HOST_PASSWORD = 'berylliumguacamoleb'
EMAIL_PORT = 587
DEFAULT_FROM_EMAIL  = 'communities.atria@gmail.com'


LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

