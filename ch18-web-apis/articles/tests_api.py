from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Article


class ArticleAPITests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username="testuser",
            password="testpass123",
        )
        cls.article = Article.objects.create(
            title="A sample article",
            body="Some interesting content.",
            author=cls.user,
        )

    def test_api_list_view(self):
        response = self.client.get(reverse("article_api_list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["title"], "A sample article")

    def test_api_detail_view(self):
        url = reverse("article_api_detail", kwargs={"pk": self.article.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["author"], "testuser")

    def test_api_create_requires_login(self):
        response = self.client.post(
            reverse("article_api_list"),
            {"title": "New article", "body": "New content."},
        )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_api_create_sets_author(self):
        self.client.login(username="testuser", password="testpass123")
        response = self.client.post(
            reverse("article_api_list"),
            {"title": "New article", "body": "New content."},
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["author"], "testuser")
        self.assertEqual(Article.objects.count(), 2)