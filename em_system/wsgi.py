import os

from configurations import importer
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "em_system.settings")
os.environ.setdefault("DJANGO_CONFIGURATION", "Production")

importer.install()

application = get_wsgi_application()
