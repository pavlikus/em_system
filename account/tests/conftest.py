import pytest
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient


AuthUser = get_user_model()


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def test_user():
    return {"email": "test@test.com", "password": "test_123"}


@pytest.fixture
def test_new_user():
    return {
        "email": "test2@test.com",
        "password": "test_123",
        "password_confirmation": "test_123",
    }


@pytest.fixture
def test_auth_user(test_user):
    return AuthUser.objects.create_user(**test_user)


@pytest.fixture
def auth_client(api_client, test_auth_user):
    api_client.force_authenticate(user=test_auth_user)
    return api_client
