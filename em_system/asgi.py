import os

from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "em_system.settings")
os.environ.setdefault("DJANGO_CONFIGURATION", "Production")

application = get_asgi_application()
