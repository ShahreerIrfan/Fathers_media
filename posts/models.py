# posts/models.py

from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model

class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    image = models.ImageField(upload_to='photos/post_photo', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(get_user_model(), related_name='liked_posts', blank=True)

    def __str__(self):
        return f'{self.user.username} - {self.created_at}'
    


    
