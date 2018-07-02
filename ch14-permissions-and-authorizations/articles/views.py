from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.core.exceptions import PermissionDenied

from . import models


class ArticleListView(LoginRequiredMixin, ListView):
    model = models.Article
    template_name = 'article_list.html'
    login_url = 'login'

    # def get_queryset(self):
    # queryset = self.get_queryset().filter(author=self.request.user)
    # return queryset


class ArticleDetailView(LoginRequiredMixin, DetailView):
    model = models.Article
    template_name = 'article_detail.html'
    login_url = 'login'


# class AuthorRequiredMixin(object):
#     def dispatch(self, request, *args, **kwargs):
#         if self.object.author != self.request.user:
#             return HttpResponseForbidden()
#         return super(AuthorRequiredMixin, self).dispatch(request, *args, **kwargs)

class CheckOwnerMixin:
    # To be used with classes derived from SingleObjectMixin
    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if not obj.author == self.request.user:
            raise PermissionDenied
        return obj


# class AuthorOnlyMixin(AccessMixin):
#     """Verify that the current user is authenticated."""

#     def dispatch(self, request, *args, **kwargs):
#         if not self.request.author == request.user:
#             return self.handle_no_permission()
#         return super().dispatch(request, *args, **kwargs)


class ArticleUpdateView(LoginRequiredMixin, CheckOwnerMixin, UpdateView):
    model = models.Article
    fields = ['title', 'body', ]
    template_name = 'article_edit.html'
    login_url = 'login'

    # def test_func(self):
    #     return self.author == self.request.user


class ArticleDeleteView(LoginRequiredMixin, DeleteView):
    model = models.Article
    template_name = 'article_delete.html'
    success_url = reverse_lazy('article_list')
    login_url = 'login'


class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = models.Article
    template_name = 'article_new.html'
    fields = ['title', 'body', ]
    login_url = 'login'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
