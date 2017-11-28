from django.views.generic import ListView
from .models import Post


class Home_page_view(ListView):
    model = Post
    template_name = 'message_app/index.html'
