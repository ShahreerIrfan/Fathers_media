# posts/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_post, name='create_post'),
    # Add other post-related URLs as needed
]
