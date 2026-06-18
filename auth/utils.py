from django.utils import timezone
from rest_framework.response import Response

from auth import settings


def set_cookies(response: Response, token: str) -> None:
    cookie_name = settings.DEFAULTS["COOKIE_NAME"]
    token_expiration = timezone.now() + settings.DEFAULTS["TOKEN_LIFETIME"]
    cookie_secure = settings.DEFAULTS["SECURE"]
    cookie_httponly = settings.DEFAULTS["HTTPONLY"]
    cookie_samesite = settings.DEFAULTS["SAMESITE"]
    cookie_domain = settings.DEFAULTS["COOKIE_DOMAIN"]

    if cookie_name:
        response.set_cookie(
            cookie_name,
            token,
            expires=token_expiration,
            secure=cookie_secure,
            httponly=cookie_httponly,
            samesite=cookie_samesite,
            domain=cookie_domain,
        )


def unset_cookies(response: Response) -> None:
    cookie_name = settings.DEFAULTS["COOKIE_NAME"]
    cookie_samesite = settings.DEFAULTS["SAMESITE"]
    cookie_domain = settings.DEFAULTS["COOKIE_DOMAIN"]

    if cookie_name:
        response.delete_cookie(
            cookie_name, samesite=cookie_samesite, domain=cookie_domain
        )
