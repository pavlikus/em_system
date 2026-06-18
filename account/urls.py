from django.urls import path

from account.views import RegistrationView

app_name = "account"


urlpatterns = [
    path("registration/", RegistrationView.as_view(), name="registration"),
]
