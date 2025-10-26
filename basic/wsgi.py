"""
WSGI config for basic project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os

import importlib

# Import Django's WSGI application dynamically to avoid static import resolution errors in some editors/environments
_wsgi = importlib.import_module('django.core.wsgi')
get_wsgi_application = getattr(_wsgi, 'get_wsgi_application')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'basic.settings')

application = get_wsgi_application()
