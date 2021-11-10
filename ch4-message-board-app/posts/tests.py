from django.test import TestCase
from django.urls import reverse  # new
from .models import Post


class PostsTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.post = Post.objects.create(text="This is a test!")

    def test_post_content(self):
        self.assertEqual(self.post.text, "This is a test!")

    def test_homepage_status_code(self):  # new
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_homepage_uses_correct_template(self):  # new
        response = self.client.get(reverse("home"))
        self.assertTemplateUsed(response, "home.html")

    def test_homepage_content(self):  # new
        response = self.client.get(reverse("home"))
        self.assertContains(response, "This is a test!")
