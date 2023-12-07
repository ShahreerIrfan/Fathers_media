from django import forms
from .models import Post,Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['content', 'image']

class LikeForm(forms.Form):
    pass  # Your existing like form code





class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']