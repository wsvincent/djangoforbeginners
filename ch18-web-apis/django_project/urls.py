from django.conf import settings  # new
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    path("accounts/", include("accounts.urls")),
    path("articles/", include("articles.urls")),
    path("", include("pages.urls")),
    path("api/v1/", include("articles.api_urls")),  # new
    path("api-auth/", include("rest_framework.urls")),  # new
]

if settings.DEBUG:
    urlpatterns += [path("__debug__/", include("debug_toolbar.urls"))]
