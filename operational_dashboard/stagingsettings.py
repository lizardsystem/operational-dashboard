# (c) Nelen & Schuurmans.  GPL licensed, see LICENSE.rst.

from operational_dashboard.settings import *

DATABASES = {
    # Changed server from production to staging
    'default': {
        'NAME': 'operational_dashboard',
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'USER': 'operational_dashboard',
        'PASSWORD': 'imk*)8ena!',
        'HOST': 's-web-db-00-d03.external-nens.local',
        'PORT': '5432',
        },
    }

# TODO: Put your real url here to configure Sentry.
# RAVEN_CONFIG = {
#     'dsn': ('http://some:hash@your.sentry.site/some_number')}

# TODO: add staging gauges ID here.
UI_GAUGES_SITE_ID = ''  # Staging has a separate one.

# Add your staging name here. Django 1.6+
ALLOWED_HOSTS = ['operational-dashboard.staging.lizard.net']
