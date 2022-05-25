from django.db import models


class Article(models.Model):
    content = models.TextField()
    Title = models.TextField()
