# posts/views.py

from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from django.http import JsonResponse
import random
from django.core.paginator import Paginator

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

# posts/views.py



# views.py



# views.py

from django.shortcuts import render
from .models import Post
import random

def post_list(request):
    # Retrieve all posts from the database as a list
    all_posts = list(Post.objects.all())

    # Shuffle the list of posts randomly
    random.shuffle(all_posts)

    # Render the post page with the shuffled posts
    return render(request, 'posts/post_list.html', {'posts': all_posts})







# Like system

# posts/views.py



def like_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.user in post.likes.all():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True

    return JsonResponse({'liked': liked, 'likes_count': post.likes.count})



