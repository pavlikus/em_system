import json
from typing import Self

import pyseto
from django.utils.translation import gettext_lazy as _
from pyseto import Key

from . import settings
from .exceptions import TokenError


class Token:
    def __init__(
        self: Self, payload: dict | None = None, raw_token: str | None = None
    ) -> None:
        self.key = Key.new(
            version=settings.DEFAULTS["VERSION"],
            purpose="local",
            key=settings.DEFAULTS["SECRET_KEY"].encode(),
        )
        if payload is not None:
            self.payload = payload
            self._create_token()
        elif raw_token is not None:
            self.token = raw_token
            self._verify()
        else:
            raise TokenError(_("Missing argument 'payload' or 'token'"))

    def _create_token(self: Self) -> None:
        exp = int(settings.DEFAULTS["TOKEN_LIFETIME"].total_seconds())
        self.token = pyseto.encode(
            self.key,
            self.payload,
            serializer=json,
            exp=exp,
        ).decode()

    def _verify(self: Self) -> None:
        try:
            self.payload = pyseto.decode(
                self.key, self.token, deserializer=json
            ).payload
        except (ValueError, pyseto.exceptions.PysetoError):
            raise TokenError(_("Token is invalid or expired")) from None
