from django.conf.urls import url
from . views import BlogListView, BlogDetailView, BlogCreateView, BlogUpdateView, BlogDeleteView

urlpatterns = [
    url(r'^$',
        BlogListView.as_view(), name='post_list'),

    url(r'^post/(?P<pk>\d+)/$',
        BlogDetailView.as_view(), name='post_detail'),

    url(r'^post/new/$',
        BlogCreateView.as_view(), name='post_new'),

    url(r'^post/(?P<pk>\d+)/edit/$',
        BlogUpdateView.as_view(), name='post_edit'),

    url(r'^author/(?P<pk>\d+)/delete/$',
        BlogDeleteView.as_view(), name='post_delete'),
]
