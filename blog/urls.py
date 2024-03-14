from django.urls import path
from blog import views


urlpatterns = [
    # path('', views.index, name='index'),
    path('posts/', views.PostListView.as_view(), name='index'),
    # path('new/', views.new_post, name='create'),
    path('posts/new/', views.PostCreateView.as_view(), name='create'),
    # path('posts/<int:post_id>/', views.detail, name='detail'),
    path('posts/<int:pk>/', views.PostDetailView.as_view(), name='detail'),
    # path('posts/comment', views.create_comment, name='comment')
    path('posts/comment', views.CommentCreateView.as_view(), name='comment')
]
