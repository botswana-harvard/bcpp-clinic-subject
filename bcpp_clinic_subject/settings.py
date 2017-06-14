'''
Django settings for bcpp_clinic project.

Generated by 'django-admin startproject' using Django 1.9.7.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
'''
import configparser
import os
import sys

from django.core.management.color import color_style
from pathlib import PurePath

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.realpath(__file__))

style = color_style()

APP_NAME = 'bcpp_clinic_subject'

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '*3izpxc9!j7)(a*2+_sw%_10gx*_$z1-%bf2mz%!pkd%@*%$1)'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

CONFIG_FILE = '{}.conf'.format(APP_NAME)
if DEBUG:
    ETC_DIR = str(PurePath(BASE_DIR).joinpath('etc'))
else:
    ETC_DIR = '/etc'
ALLOWED_HOSTS = ['127.0.0.1', 'localhost']

CONFIG_PATH = os.path.join(ETC_DIR, APP_NAME, CONFIG_FILE)
sys.stdout.write(style.SUCCESS('Reading config from {}\n'.format(CONFIG_PATH)))

config = configparser.RawConfigParser()
config.read(os.path.join(CONFIG_PATH))

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'tz_detect',
    'rest_framework',
    'rest_framework.authtoken',
    'django_crypto_fields.apps.AppConfig',
    'django_revision.apps.AppConfig',
    'edc_consent.apps.AppConfig',
    'edc_search.apps.AppConfig',
    'edc_locator.apps.AppConfig',
    'edc_registration.apps.AppConfig',
    'edc_visit_schedule.apps.AppConfig',
    'edc_offstudy.apps.AppConfig',
    'bcpp_clinic.apps.EdcIdentifierAppConfig',
    'bcpp_clinic.apps.EdcDeviceAppConfig',
    'bcpp_clinic.apps.EdcProtocolAppConfig',
    'bcpp_clinic.apps.EdcLabAppConfig',
    'bcpp_clinic.apps.EdcMetadataAppConfig',
    'bcpp_clinic.apps.EdcVisitTrackingAppConfig',
    'bcpp_clinic.apps.EdcTimepointAppConfig',
    'bcpp_clinic.apps.EdcAppointmentAppConfig',
    'bcpp_clinic.apps.EdcSyncAppConfig',
    'bcpp_clinic.apps.EdcSyncFilesAppConfig',
    'bcpp_clinic_subject.apps.AppConfig',
    'bcpp_clinic_screening.apps.AppConfig',
    'bcpp_clinic_validations.apps.AppConfig'
]


if 'test' in sys.argv:
    MIGRATION_MODULES = {
        'django_crypto_fields': None,
        'bcpp_clinic_subject': None,
        'edc_appointment': None,
        'edc_consent': None,
        'edc_locator': None,
        'edc_offstudy': None,
        'edc_death_report': None,
        'edc_identifier': None,
        'edc_lab': None,
        'edc_metadata': None,
        'edc_registration': None,
        'edc_sync': None,
        'admin': None,
        'auth': None,
        'edc_sync_files': None,
        'sessions': None,
    }

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'bcpp_clinic_subject.urls'

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

WSGI_APPLICATION = 'bcpp_clinic_subject.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Africa/Gaborone'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/
STATIC_ROOT = os.path.join(BASE_DIR, APP_NAME, 'static')
STATIC_URL = '/static/'
MEDIA_ROOT = os.path.join(BASE_DIR, APP_NAME, 'media')

MEDIA_URL = '/media/'

GIT_DIR = BASE_DIR

KEY_PATH = os.path.join(str(PurePath(BASE_DIR).parent), 'crypto_fields')

CURRENT_MAP_AREA = 'test_community'
DEVICE_ID = '21'
DEVICE_ROLE = 'Client'
LABEL_PRINTER = 'label_printer'
