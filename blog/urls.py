from django.urls import path
from blog import views


urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.new_post, name='create'),
    path('posts/<int:post_id>/', views.detail, name='detail'),
    path('posts/comment', views.create_comment, name='comment')
]
