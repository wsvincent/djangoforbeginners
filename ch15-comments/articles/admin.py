from django.contrib import admin

from . import models


class CommentInline(admin.TabularInline):
    model = models.Comment


class ArticleAdmin(admin.ModelAdmin):
    inlines = [
        CommentInline,
    ]


admin.site.register(models.Article, ArticleAdmin)
admin.site.register(models.Comment)
