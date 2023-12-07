# posts/models.py

from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.contrib.auth.models import User

class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='post_comments')
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.created_at}"
        

class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    image = models.ImageField(upload_to='post_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='liked_posts', blank=True)
    comments = models.ManyToManyField(settings.AUTH_USER_MODEL, through='Comment', related_name='commented_posts', blank=True)
    def __str__(self):
        return f'{self.user.username} - {self.content} - {self.created_at}'
    

    

# 
    
