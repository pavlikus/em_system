from datetime import timedelta

from django.conf import settings

user_settings = getattr(settings, "PASETO_AUTH", {})

DEFAULTS = {
    "SECRET_KEY": user_settings.get("SECRET_KEY", settings.SECRET_KEY),
    "COOKIE_NAME": user_settings.get("COOKIE_NAME", "token"),
    "VERSION": user_settings.get("VERSION", 4),
    "TOKEN_LIFETIME": user_settings.get("TOKEN_LIFETIME", timedelta(days=30)),
    "SECURE": user_settings.get("SECURE", False),
    "HTTPONLY": user_settings.get("HTTPONLY", True),
    "SAMESITE": user_settings.get("SAMESITE", "Lax"),
    "COOKIE_DOMAIN": user_settings.get("COOKIE_DOMAIN", None),
}
