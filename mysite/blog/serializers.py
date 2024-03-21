from blog.models import Post, Comment
from rest_framework import serializers


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'content', 'demo_content']


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment

        fields = ['post', 'content']
