from django.contrib.auth import get_user_model
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from . import models


class PostListView(ListView):
    model = models.Post
    template_name = 'post_list.html'


class PostCreateView(CreateView):
    model = models.Post
    template_name = 'post_new.html'
    fields = ['message', 'author']

    # def form_valid(self, form):
    #     form.instance.created_by = self.request.get_user_model()
    #     return super().form_valid(form)


class PostDetailView(DetailView):
    model = models.Post
    template_name = 'post_detail.html'


class PostUpdateView(UpdateView):
    model = models.Post
    fields = ['message']
    template_name = 'post_edit.html'


class PostDeleteView(DeleteView):
    model = models.Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('posts')
