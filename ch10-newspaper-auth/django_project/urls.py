from django.contrib import admin
from django.urls import include, path  # new
from django.views.generic import TemplateView  # new

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),  # new
    path("accounts/", include("accounts.urls")),  # new
    path("", TemplateView.as_view(template_name="home.html"), name="home"),  # new
]
