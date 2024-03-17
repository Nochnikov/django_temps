from django.forms import model_to_dict
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework import status

from rest_framework.decorators import api_view
from rest_framework.response import Response
from blog.serializers import PostSerializer, CommentSerializer
from blog.models import Post, Comment


# Create your views here.

@api_view(["GET", "POST"])
def index(request):
    if request.method == 'POST':
        print(request.POST)
        # print(request.body)
        instance = PostSerializer(data=request.POST)

        if instance.is_valid():
            instance.save()
            # post.author_id = 1
            # post.save()
        return Response(instance.data, status=status.HTTP_201_CREATED)
    elif request.method == 'GET':
        post_id = request.GET.get('post_id')
        post = Post.objects.get(pk=post_id)

        # return HttpResponse('Hello World!', content_type='application/json')

        data = {}

        if post:
            instance = PostSerializer(post)
            # data = PostSerializer(post)
            # data = model_to_dict(post, fields=['id', 'title', 'content'])

            # data['id'] = post.id
            # data['title'] = post.title
            # data['content'] = post.content

            # как только мы скачали допфреймворк django rest framework JsonResponse меняется на просто Response
            # return JsonResponse(data)
            print(instance.data)
            return Response(instance.data)
        return Response({'detail': 'Post does not exist', 'status': status.HTTP_404_NOT_FOUND})


@api_view(["GET", "POST"])
def comment(request):
    if request.method == 'POST':
        instance = CommentSerializer(data=request.POST)

        if instance.is_valid():
            instance.save()

        return Response(instance.data, status=status.HTTP_201_CREATED)

    elif request.method == 'GET':
        comment_id = request.GET.get('comment_id')
        comments = Comment.objects.get(pk=comment_id)

        if comments:
            instance = CommentSerializer(comments)

            return Response(instance.data)
        return Response(status.HTTP_404_NOT_FOUND)
