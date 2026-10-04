from django.urls import path

from .views import about_page_view, home_page_view  # new

urlpatterns = [
    path("about/", about_page_view),  # new
    path("", home_page_view), 
]