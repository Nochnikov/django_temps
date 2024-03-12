from django.urls import path
from blog import views


urlpatterns = [
    path('', views.index),
    path('posts/<int:post_id>/', views.detail)
]
