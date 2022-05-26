from django.contrib import admin

# Register your models here.
from articles.models import Article


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'id']
    search_fields = ['title']


admin.site.register(Article, ArticleAdmin)
