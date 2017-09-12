from django.views.generic import ListView, DetailView

from . models import Post


class BlogListView(ListView):
    model = Post
    template = 'post_list.html'


class BlogDetailView(DetailView):
    model = Post
    template = 'post_detail.html'
