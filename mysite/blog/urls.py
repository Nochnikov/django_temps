from django.urls import path

from blog import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.index, name='index'),
    path('comment/', views.comment, name='comment')
]