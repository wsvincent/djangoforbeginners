from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Article


class ArticleTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="testuser",
            email="testuser@email.com",
            password="testpass123",
        )
        self.article = Article.objects.create(
            title="A sample article",
            body="Some interesting content.",
            author=self.user,
        )

    def test_article_model(self):
        self.assertEqual(self.article.title, "A sample article")
        self.assertEqual(self.article.body, "Some interesting content.")
        self.assertEqual(self.article.author.username, "testuser")
        self.assertEqual(str(self.article), "A sample article")
        self.assertEqual(self.article.get_absolute_url(), f"/articles/{self.article.pk}/")

    def test_article_list_view(self):
        response = self.client.get(reverse("article_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "A sample article")
        self.assertTemplateUsed(response, "article_list.html")

    def test_article_detail_view(self):
        response = self.client.get(self.article.get_absolute_url())
        no_response = self.client.get("/articles/100000/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, "A sample article")
        self.assertTemplateUsed(response, "article_detail.html")
