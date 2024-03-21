from django.forms import model_to_dict
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from blog.serializers import PostSerializer, CommentSerializer
from blog.models import Post, Comment


# Create your views here.


# class PostGetUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#     lookup_field = 'pk'
# и такое существует


class PostDetailView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'pk'


class PostCreateView(generics.CreateAPIView):
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content', None)

        if content == "":
            content = title

        serializer.save(author_id=1, content=content)


class PostListView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostListCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(author_id=1)


class PostUpdateView(generics.UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'pk'

    # def perform_update(self, serializer):
    #     pass


class PostDeleteView(generics.DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'pk'


class CommentCreateView(generics.CreateAPIView):
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        content = serializer.validated_data.get("content")

        serializer.save(author_id=1)


class CommentDetailView(generics.RetrieveAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    lookup_field = 'pk'


class CommentListView(generics.ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentUpdateView(generics.UpdateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    lookup_field = 'pk'


class CommentDeleteView(generics.DestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    lookup_field = 'pk'

# @api_view(["GET", "POST"])
# def index(request):
#     if request.method == 'POST':
#         print(request.POST)
#         # print(request.body)
#         instance = PostSerializer(data=request.POST)
#
#         if instance.is_valid():
#             instance.save()
#             # post.author_id = 1
#             # post.save()
#         return Response(instance.data, status=status.HTTP_201_CREATED)
#     elif request.method == 'GET':
#         post_id = request.GET.get('post_id')
#         if post_id is not None:
#                post = Post.objects.get(pk=post_id)
#       if post:
#                      instance = PostSerializer(post)
#                           return Response(instance.data)
#          else:
#                 posts = Post.objects.all()
#                 if posts:
#                     instance = PostSerializer(posts, many=True)
#                     return Response(instance.data)
#         # return HttpResponse('Hello World!', content_type='application/json')
#
#         data = {}
#
#             # data = PostSerializer(post)
#             # data = model_to_dict(post, fields=['id', 'title', 'content'])
#
#             # data['id'] = post.id
#             # data['title'] = post.title
#             # data['content'] = post.content
#
#             # как только мы скачали допфреймворк django rest framework JsonResponse меняется на просто Response
#             # return JsonResponse(data)
#             print(instance.data)
#         return Response({'detail': 'Post does not exist', 'status': status.HTTP_404_NOT_FOUND})
#
#
# @api_view(["GET", "POST"])
# def comment(request):
#     if request.method == 'POST':
#         instance = CommentSerializer(data=request.POST)
#
#         if instance.is_valid():
#             instance.save()
#
#         return Response(instance.data, status=status.HTTP_201_CREATED)
#
#     elif request.method == 'GET':
#         comment_id = request.GET.get('comment_id')

#         comments = Comment.objects.get(pk=comment_id)
#
#         if comments:
#             instance = CommentSerializer(comments)
#
#             return Response(instance.data)
#         return Response(status.HTTP_404_NOT_FOUND)
