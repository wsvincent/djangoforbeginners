from rest_framework import generics

from .models import Article
from .serializers import ArticleSerializer


class ArticleAPIListView(generics.ListCreateAPIView):
    queryset = Article.objects.select_related("author").prefetch_related(
        "comment_set__author"
    )
    serializer_class = ArticleSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class ArticleAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.select_related("author").prefetch_related(
        "comment_set__author"
    )
    serializer_class = ArticleSerializer
