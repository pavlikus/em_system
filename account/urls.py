from django.urls import path

from account.views import LoginView
from account.views import LogoutView
from account.views import RegistrationView
from account.views import UserDetailsView

app_name = "account"


urlpatterns = [
    path("registration/", RegistrationView.as_view(), name="registration"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("user/", UserDetailsView.as_view(), name="user"),
]
