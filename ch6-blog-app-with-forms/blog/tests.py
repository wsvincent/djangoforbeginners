from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Post


class BlogTests(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create(username="wsv")
        Post.objects.create(
            title="my title",
            author=self.user,
            body="just a test"
        )

    def test_string_representation(self):
        post = Post(title="My entry title")
        self.assertEqual(str(post), post.title)

    def test_post_content(self):
        post = Post.objects.get(id=1)
        self.assertEqual(f'{post.title}', "my title")
        self.assertEqual(f'{post.author}', "wsv")
        self.assertEqual(f'{post.body}', "just a test")

    def test_post_list_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'just a test')
        self.assertTemplateUsed(response, 'home.html')

    def test_post_detail_view(self):
        response = self.client.get('/post/1/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'my title')
        self.assertTemplateUsed(response, 'post_detail.html')

    # def test_post_create_view(self):
    #     response = self.client.post(
    #         '/post/new/', {'author': self.user, 'title': 'Test title', 'body': 'My body text'})
    #     self.assertEqual(Post.objects.last().author, 'wsv')
    #     self.assertEqual(Post.objects.last().title, 'Test title')
    #     self.assertEqual(Post.objects.last().body, 'My body text')
