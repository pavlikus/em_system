from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny

from account.serializers import RegistrationSerializer


class RegistrationView(CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = RegistrationSerializer
