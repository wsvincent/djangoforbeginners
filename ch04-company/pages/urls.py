from django.urls import path

from .views import AboutPageView, home_page_view

urlpatterns = [
    path("about/", AboutPageView.as_view(), name="about"),  # new
    path("", home_page_view, name="home"),  # new
]
