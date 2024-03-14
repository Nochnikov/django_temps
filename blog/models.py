from datetime import datetime, timedelta

from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class NewPostManager(models.Manager):

    def get_queryset(self):
        return super().get_queryset().filter(created_at__gte=datetime.now() - timedelta(hours=24))


class SelectIntroManager(models.Manager):

    def get_queryset(self):
        return super().get_queryset().filter(categories__name__icontains='intro')


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Id: {self.pk}. Name: {self.name}"


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    title = models.CharField(max_length=200, db_index=True)
    content = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField(Category)

    new_posts = NewPostManager()
    intro_in_content = SelectIntroManager()
    objects = models.Manager()

    def is_updated(self):
        return self.created_at != self.updated_at

    def __str__(self):
        return f"{self.pk},{self.title}"

    # def __str__(self):
    #     return f"{self.pk}"

    class Meta:
        db_table = 'posts'
        ordering = ['title']
        unique_together = ('title', 'content')
        indexes = [
            models.Index(fields=['title', 'content'])
        ]
        constraints = []
        default_related_name = 'posts'


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    content = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.content}"


# class UserInfo(models.Model):
#     first_name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=100)
#
#     class Meta:
#         abstract = True
#

class TestUser(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField(default=18)

    def __str__(self):
        return f"{self.name}"
