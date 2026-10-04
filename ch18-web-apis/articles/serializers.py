from rest_framework import serializers

from .models import Article, Comment  # new


class CommentSerializer(serializers.ModelSerializer):  # new
    author = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Comment
        fields = ("id", "comment", "author")


class ArticleSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    comments = CommentSerializer(  # new
        source="comment_set", many=True, read_only=True
    )

    class Meta:
        model = Article
        fields = ("id", "title", "body", "date", "author", "comments")  # new
