from django.db import models

from datetime import datetime, timedelta

from django.contrib.auth.models import User
from django.db import models


# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Name: {self.name}. Description: {self.description}"


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    title = models.CharField(max_length=200, db_index=True)
    content = models.TextField(blank=True, null=True)
    photo = models.ImageField(upload_to="images/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField(Category)

    @property
    def demo_content(self):
        return f"{self.content[:10]}..."

    def is_updated(self):
        return self.created_at != self.updated_at

    def __str__(self):
        return f"{self.pk},{self.title}"

    class Meta:
        ordering = ['title']
        unique_together = ('title', 'content')
        indexes = [

            models.Index(fields=['title', 'content'])
        ]
        default_related_name = 'posts'


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    content = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.content}"

