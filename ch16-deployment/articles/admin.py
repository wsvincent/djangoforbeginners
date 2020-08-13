from django.contrib import admin
from .models import Article, Comment


class CommentInline(admin.TabularInline): # new
    model = Comment


class ArticleAdmin(admin.ModelAdmin): # new
    inlines = [
        CommentInline,
    ]


admin.site.register(Article, ArticleAdmin) # new
admin.site.register(Comment)
