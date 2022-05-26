from django.contrib import admin
from django.urls import path

from .views import article_detail_view, article_search_view, article_create_view

urlpatterns = [

    path('detail/<int:pk>/', article_detail_view, name="article-detail"),
    path('search/', article_search_view, name="search-article"),
    path('create/', article_create_view, name="create-article"),
]
