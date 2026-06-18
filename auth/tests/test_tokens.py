import pytest
from django.test import TestCase

from auth.exceptions import TokenError
from auth.tokens import Token


class TokenTest(TestCase):
    def setUp(self):
        self.payload = {"pk": 1, "email": "test@test.com"}

    def test_token_success_creation(self):
        Token(payload=self.payload)

    def test_token_exception(self):
        _token = Token(payload=self.payload)
        token = _token.token[:-16]
        with pytest.raises(TokenError):
            Token(raw_token=token)

    def test_token_init_exception(self):
        with pytest.raises(TokenError):
            Token()

    def test_token_invalid(self):
        token = "invalid_token"
        with pytest.raises(TokenError):
            Token(raw_token=token)
