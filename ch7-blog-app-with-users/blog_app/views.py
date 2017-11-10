from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from . models import Post


class BlogListView(ListView):
    model = Post
    template_name = 'blog_app/post_list.html'


class BlogDetailView(DetailView):
    model = Post
    template_name = 'blog_app/post_detail.html'


class BlogCreateView(CreateView):
    model = Post
    template_name = 'blog_app/post_new.html'
    fields = '__all__'


class BlogUpdateView(UpdateView):
    model = Post
    fields = ['title', 'text']
    template_name = 'blog_app/post_edit.html'


class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'blog_app/post_delete.html'
    success_url = reverse_lazy('post_list')
