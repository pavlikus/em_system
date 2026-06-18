from typing import Self

from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from rest_framework import authentication
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.request import Request

from . import settings
from .exceptions import TokenError
from .tokens import Token

AuthUser = get_user_model()


class PasetoAuthentication(authentication.BaseAuthentication):
    """
    Paseto authentication.
    """

    def authenticate(self: Self, request: Request) -> tuple | None:
        """
        Checks that the authentication token provided in a request cookie
        (and through the header as normal, with a preference to the header).

        Returns:
            A tuple with the authenticated user and the access token.
        """
        cookie_name = settings.DEFAULTS["COOKIE_NAME"]
        if cookie_name:
            raw_token = request.COOKIES.get(cookie_name)
        else:
            return None

        if raw_token is None:
            return None

        try:
            validated_token = Token(raw_token=raw_token)
        except TokenError:
            return None

        return self.get_user(validated_token), validated_token

    def get_user(self, validated_token: Token) -> AuthUser:
        """
        Attempts to find and return a user using the given validated token.
        """
        try:
            pk = validated_token.payload["pk"]
        except KeyError:
            raise AuthenticationFailed(
                _("Token is invalid"), code="invalid_token"
            ) from None

        try:
            user = AuthUser.objects.get(pk=pk)
        except AuthUser.DoesNotExist:
            raise AuthenticationFailed(
                _("User not found"), code="user_not_found"
            ) from None

        if not user.is_active:
            raise AuthenticationFailed(
                _("User is inactive"), code="user_inactive"
            )

        return user
