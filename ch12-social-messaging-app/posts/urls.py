from django.urls import path

from . import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='posts'),
    path('new/', views.PostCreateView.as_view(), name='post_new'),
    path('<int:pk>/edit/',
         views.PostUpdateView.as_view(), name='post_edit'),
    path('<int:pk>/',
         views.PostDetailView.as_view(), name='post_detail'),
    path('<int:pk>/delete/',
         views.PostDeleteView.as_view(), name='post_delete'),
]
