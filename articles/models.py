from django.db import models


class Article(models.Model):
    content = models.TextField()
    title = models.TextField()

    def __str__(self):
        return self.title
