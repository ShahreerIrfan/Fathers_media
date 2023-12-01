# posts/views.py

from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm
from django.contrib.auth.decorators import login_required

@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('home')  # Change 'home' to the name of your home page URL
    else:
        form = PostForm()

    return render(request, 'posts/create_post.html', {'form': form, 'user': request.user})
