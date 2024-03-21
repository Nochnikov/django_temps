from django.urls import path

from blog import views

urlpatterns = [
    path('', views.PostListCreateView.as_view()),
    path('<int:pk>/', views.PostDetailView.as_view(), name='detail'),
    path('<int:pk>/delete/', views.PostDeleteView.as_view(), name='delete'),
    path('<int:pk>/update/', views.PostUpdateView.as_view(), name='update'),
    path('comment/', views.CommentCreateView.as_view(), name='create_comment'),
    path('comment/<int:pk>/', views.CommentDetailView().as_view(), name='comment_detail'),
    path('comment/list/', views.CommentListView.as_view(), name='comment_list'),
    path('comment/<int:pk>/update/', views.CommentUpdateView.as_view(), name='update_comment'),
    path('comment/<int:pk>/delete/', views.CommentDeleteView.as_view(), name='delete_comment'),
]