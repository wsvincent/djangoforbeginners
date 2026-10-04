from django.urls import path

from .api_views import ArticleAPIDetailView, ArticleAPIListView

urlpatterns = [
    path("articles/", ArticleAPIListView.as_view(), name="article_api_list"),
    path(
        "articles/<int:pk>/",
        ArticleAPIDetailView.as_view(),
        name="article_api_detail",
    ),
]
