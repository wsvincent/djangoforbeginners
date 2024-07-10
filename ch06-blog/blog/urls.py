from django.urls import path
from .views import post_list, post_detail  # new

urlpatterns = [
    path("post/<int:pk>/", post_detail, name="post_detail"),  # new
    path("", post_list, name="home"),
]
