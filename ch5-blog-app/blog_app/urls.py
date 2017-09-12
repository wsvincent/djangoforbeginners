from django.conf.urls import url
from . views import BlogListView, BlogDetailView

urlpatterns = [
    url(r'^$', BlogListView.as_view(), name='post_list'),
    url(r'^post/(?P<pk>\d+)/$', BlogDetailView.as_view(), name='post-detail'),
]
