from django.contrib import admin
from django.urls import path

from .views import article_detail_view

urlpatterns = [

    path('detail/<int:pk>', article_detail_view, name="article-detail"),
]
