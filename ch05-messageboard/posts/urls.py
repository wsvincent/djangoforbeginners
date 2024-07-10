from django.urls import path

# from .views import post_list
from .views import PostList  # new

urlpatterns = [
    # path("", post_list, name="post_list"),
    path("", PostList.as_view(), name="home"),  # new
]
