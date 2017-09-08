from django.conf.urls import url

from .views import Home_page_view, About_page_view

urlpatterns = [
    url(r'^$', Home_page_view.as_view()),
    url(r'^about', About_page_view.as_view()),
]
