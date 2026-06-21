import pytest
from django.urls import reverse
from rest_framework import status


@pytest.mark.django_db
@pytest.mark.usefixtures("test_auth_user")
def test_login(test_user, api_client):
    url = reverse("account:login")
    response = api_client.post(url, test_user)
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_registration(test_new_user, api_client):
    url = reverse("account:registration")
    response = api_client.post(url, test_new_user)
    assert response.status_code == status.HTTP_201_CREATED


@pytest.mark.django_db
def test_unauthenticated_request(api_client):
    url = reverse("account:user")
    response = api_client.get(url)
    assert response.status_code == status.HTTP_403_FORBIDDEN


@pytest.mark.django_db
def test_authenticated_request(auth_client):
    url = reverse("account:user")
    response = auth_client.get(url)
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_users_endpoint_for_user(auth_client):
    url = reverse("users-list")
    response = auth_client.get(url)
    assert response.status_code == status.HTTP_403_FORBIDDEN


@pytest.mark.django_db
def test_users_endpoint_request(api_client):
    url = reverse("users-list")
    response = api_client.get(url)
    assert response.status_code == status.HTTP_403_FORBIDDEN


@pytest.mark.django_db
def test_users_endpoint_for_staff(auth_staff_client):
    url = reverse("users-list")
    response = auth_staff_client.get(url)
    assert response.status_code == status.HTTP_200_OK
