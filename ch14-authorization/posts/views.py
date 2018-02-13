from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from . import models


class PostListView(LoginRequiredMixin, ListView):
    model = models.Post
    template_name = 'post_list.html'
    login_url = 'login'


class PostCreateView(LoginRequiredMixin, CreateView):
    model = models.Post
    template_name = 'post_new.html'
    fields = ['message']
    login_url = 'login'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostDetailView(LoginRequiredMixin, DetailView):
    model = models.Post
    template_name = 'post_detail.html'
    login_url = 'login'


class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = models.Post
    fields = ['message']
    template_name = 'post_edit.html'
    login_url = 'login'


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = models.Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('posts')
    login_url = 'login'
