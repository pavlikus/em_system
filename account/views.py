from typing import Any
from typing import Self

from django.utils.translation import gettext_lazy as _
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from account.serializers import LoginSerializer
from account.serializers import RegistrationSerializer
from account.serializers import UserDetailsSerializer
from auth.tokens import Token
from auth.utils import set_cookies
from auth.utils import unset_cookies


class RegistrationView(CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = RegistrationSerializer


class LoginView(GenericAPIView):
    permission_classes = (AllowAny,)
    serializer_class = LoginSerializer
    http_method_names = ("post", "options", "head")

    def get_response(self: Self) -> Response:
        serializer_class = UserDetailsSerializer
        serializer = serializer_class(self.user)
        response = Response(serializer.data, status=status.HTTP_200_OK)
        token = Token(payload=serializer.data)
        set_cookies(response, token.token)
        return response

    def post(
        self: Self, request: Request, *args: Any, **kwargs: Any
    ) -> Response:
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.user = serializer.validated_data["user"]
        return self.get_response()


class LogoutView(APIView):
    permission_classes = (AllowAny,)
    http_method_names = ("post", "options", "head")

    def post(
        self: Self, request: Request, *args: Any, **kwargs: Any
    ) -> Response:
        response = Response(
            {"detail": _("Successfully logged out.")},
            status=status.HTTP_200_OK,
        )
        unset_cookies(response)

        return response
