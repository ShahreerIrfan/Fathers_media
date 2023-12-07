# posts/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_post, name='create_post'),
    path('', views.post_list, name='post_list'),
    # path('like/<int:post_id>/', views.like_post, name='like_post'),
    path('<int:post_id>/', views.post_detail, name='post_detail'),
    path('like_post/<int:post_id>/', views.like_post, name='like_post'),
]

# 