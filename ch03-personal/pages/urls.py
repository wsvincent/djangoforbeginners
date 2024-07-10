from django.urls import path

from .views import home_page_view, about_page_view  # new

urlpatterns = [
    path("about/", about_page_view),  # new
    path("", home_page_view),
]
