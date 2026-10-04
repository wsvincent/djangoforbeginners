from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .forms import CommentForm  # new
from .models import Article, Comment  # new


class ArticleTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="testuser",
            email="testuser@email.com",
            password="testpass123",
        )
        self.other_user = get_user_model().objects.create_user(  # new
            username="otheruser",
            email="otheruser@email.com",
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

    def test_redirect_if_not_logged_in(self):  # new
        response = self.client.get(reverse("article_list"))
        self.assertRedirects(response, "/accounts/login/?next=/articles/")

    def test_article_list_view(self):
        self.client.login(username="testuser", password="testpass123")  # new
        response = self.client.get(reverse("article_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "A sample article")
        self.assertTemplateUsed(response, "article_list.html")

    def test_article_detail_view(self):
        self.client.login(username="testuser", password="testpass123")  # new
        response = self.client.get(self.article.get_absolute_url())
        no_response = self.client.get("/articles/100000/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, "A sample article")
        self.assertTemplateUsed(response, "article_detail.html")

    def test_article_create_view(self):  # new
        self.client.login(username="testuser", password="testpass123")
        response = self.client.post(
            reverse("article_new"),
            {
                "title": "New article",
                "body": "Brand new content.",
            },
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Article.objects.last().title, "New article")
        self.assertEqual(Article.objects.last().author, self.user)

    def test_article_update_view_for_author(self):  # new
        self.client.login(username="testuser", password="testpass123")
        response = self.client.post(
            reverse("article_edit", args=[self.article.pk]),
            {"title": "Updated title", "body": "Updated body."},
        )
        self.assertEqual(response.status_code, 302)
        self.article.refresh_from_db()
        self.assertEqual(self.article.title, "Updated title")

    def test_article_update_view_forbidden_for_non_author(self):  # new
        self.client.login(username="otheruser", password="testpass123")
        response = self.client.post(
            reverse("article_edit", args=[self.article.pk]),
            {"title": "Should not save", "body": "Should not save."},
        )
        self.assertEqual(response.status_code, 403)

    def test_article_delete_view_for_author(self):  # new
        self.client.login(username="testuser", password="testpass123")
        response = self.client.post(
            reverse("article_delete", args=[self.article.pk])
        )
        self.assertRedirects(response, reverse("article_list"))

    def test_article_delete_view_forbidden_for_non_author(self):  # new
        self.client.login(username="otheruser", password="testpass123")
        response = self.client.post(
            reverse("article_delete", args=[self.article.pk])
        )
        self.assertEqual(response.status_code, 403)


class CommentTests(TestCase):  # new
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

    def test_comment_model(self):
        comment = Comment.objects.create(
            article=self.article,
            comment="A first comment",
            author=self.user,
        )
        self.assertEqual(str(comment), "A first comment")
        self.assertEqual(comment.article, self.article)
        self.assertEqual(comment.author, self.user)

    def test_article_detail_view_includes_form(self):
        self.client.login(username="testuser", password="testpass123")
        response = self.client.get(self.article.get_absolute_url())
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context["form"], CommentForm)

    def test_comment_post_creates_comment(self):
        self.client.login(username="testuser", password="testpass123")
        response = self.client.post(
            self.article.get_absolute_url(),
            {"comment": "Brand new comment"},
        )
        self.assertRedirects(response, self.article.get_absolute_url())
        self.assertEqual(self.article.comment_set.count(), 1)
        comment = self.article.comment_set.first()
        self.assertEqual(comment.comment, "Brand new comment")
        self.assertEqual(comment.author, self.user)

    def test_comment_post_requires_login(self):
        response = self.client.post(
            self.article.get_absolute_url(),
            {"comment": "Should not save"},
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.article.comment_set.count(), 0)
