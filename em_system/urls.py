import os

from django.conf import settings
from django.contrib import admin
from django.urls import include
from django.urls import path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/auth/", include("account.urls")),
]

if settings.DEBUG and os.getenv("DJANGO_CONFIGURATION") == "Development":
    from django.conf.urls.static import static
    import debug_toolbar

    urlpatterns += [
        path("__debug__/", include(debug_toolbar.urls)),
        *static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT),
    ]
