import os

from django.conf import settings
from django.contrib import admin
from django.urls import include
from django.urls import path
from rest_framework import routers

from account.views import PermissionsView
from account.views import UserViewSet

router = routers.DefaultRouter()
router.register("users", UserViewSet, basename="users")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/auth/", include("account.urls")),
    path("api/v1/permissions/", PermissionsView.as_view(), name="permissions"),
    path("api/v1/", include(router.urls)),
]

if settings.DEBUG and os.getenv("DJANGO_CONFIGURATION") == "Development":
    from django.conf.urls.static import static
    import debug_toolbar

    urlpatterns += [
        path("__debug__/", include(debug_toolbar.urls)),
        *static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT),
    ]
