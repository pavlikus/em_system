from typing import Self

from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

AuthUser = get_user_model()


class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        required=True,
        style={"input_type": "password"},
        validators=[validate_password],
    )
    password_confirmation = serializers.CharField(
        write_only=True, required=True, style={"input_type": "password"}
    )

    class Meta:
        model = AuthUser
        fields = (
            "first_name",
            "last_name",
            "middle_name",
            "email",
            "password",
            "password_confirmation",
        )

    def validate(self: Self, attrs: dict) -> dict:
        password = attrs.get("password")
        password_confirmation = attrs.get("password_confirmation")
        if password != password_confirmation:
            raise serializers.ValidationError(
                _("Password and Confirm Password Doesn't Match")
            )
        return attrs

    def create(self: Self, validated_data: dict) -> AuthUser:
        validated_data.pop("password_confirmation")
        return AuthUser.objects.create_user(**validated_data)


class UserDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthUser
        fields = ("pk", "first_name", "last_name", "middle_name", "email")
        read_only_fields = ("pk", "email")
