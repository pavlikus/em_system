from typing import Any
from typing import Self

from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):
    def create_user(
        self: Self,
        email: str,
        password: str | None = None,
        **extra_fields: Any,
    ) -> Self:
        if not email:
            raise ValueError(_("The Email field is not set"))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user


class User(AbstractUser):
    username = None
    middle_name = models.CharField(max_length=64, blank=True)
    email = models.EmailField(_("email address"), unique=True)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self: Self) -> str:
        return self.email
