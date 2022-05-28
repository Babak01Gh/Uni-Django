from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=150)
    slug = models.CharField(max_length=150, primary_key=True)
    content = models.TextField()
    publishAt = models.DateTimeField()
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
