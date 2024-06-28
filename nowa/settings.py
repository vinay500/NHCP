"""
Django settings for nowa project.

Generated by 'django-admin startproject' using Django 4.0.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""


# Project         :   Nowa - Django Bootstrap 5 Admin & Dashboard Template
# Framework       :   Django
# Django Version  :   4.0.2
# Python Version  :   3.10.1
# pip Version     :   21.3.1
# Created Date    :   29/03/2022
# Copyright       :   Spruko Technologies Private Limited
# Author          :   SPRUKO™
# Author URL      :   https://themeforest.net/user/Spruko
# Support         :   support@spruko.com
# License         :   Licensed under ThemeForest Licence


from pathlib import Path, os
from cryptography.fernet import Fernet

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')



# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-oi1lbppn9adamt-l31ias=y$-6ryq)5ce3wegyu(4gof$#gr^8'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app',
    'authentication',
    'beyond_borders',
    'community_health_cards',
    'home_care_services',
]

MIDDLEWARE = [
    
    # other middleware classes
    'htmlmin.middleware.HtmlMinifyMiddleware',
    'htmlmin.middleware.MarkRequestMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'nowa.middleware.ExceptionLoggingMiddleware',
]

ROOT_URLCONF = 'nowa.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates"],
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

WSGI_APPLICATION = 'nowa.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

# TIME_ZONE = 'Asia/Kolkata'
TIME_ZONE = 'UTC'


USE_I18N = True

USE_TZ = True

HTML_MINIFY = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'
STATIC_DIR = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = []

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# authenticating user using Email rather than Username
AUTHENTICATION_BACKENDS = [
    'authentication.authentication.EmailBackend',
    'django.contrib.auth.backends.ModelBackend',
]
# Changed User Model to CustomUser rather than 
AUTH_USER_MODEL = 'authentication.CustomUser'


# configuration for sending mail
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'care@wellnesshospitals.co.in'
# EMAIL_HOST_PASSWORD = 'lfln njqx qoln wfda'
EMAIL_HOST_PASSWORD = 'lfln njqx qoln wfd'


# key for encrypting and decrypting email and expiry time for forgot password token
EMAIL_VERIFICATION_SECRET_KEY = "4f9d3eb982fcf9c1c240d4e73f1103c8f0a1e1c7b0133b63f02d2c047b855f97"


LOG_DIR = os.path.join(BASE_DIR, 'logs')
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

# Logger: writes log records. - logger logs 
# Formatter: specifies the structure of each log record. - formatter sets log format
# Handler: determines the destination for each records. - handlers handles the logs to the file
# Filter: determines which log records get sent to the configured destination.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'syslog': {
            'level': 'INFO',
            'class': 'logging.handlers.SysLogHandler',
            'address': ('localhost', 514),
        },
        'exception_handler': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': os.path.join(LOG_DIR, 'error.log'),
            'formatter': 'standard',
        },
    },
    'formatters': {
        'standard': {
            # 'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s',
            'format': '%(asctime)s [%(filename)s:%(lineno)d] %(levelname)-8s %(message)s',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['syslog'],
            'level': 'INFO',
            'propagate': True,
        },
        'exception_logger': {
            'handlers': ['exception_handler'],
            'level': 'ERROR',
            'propagate': True,
        },
    },
}


LOGIN_URL = '/auth/signin'

# http://127.0.0.1:8000/
IP_ADDRESS = '127.0.0.1'
PORT = '8000'


NHCP_ADMIN_MAIL = 'vinaymadugula1@gmail.com'

