# posts/views.py

from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from django.http import JsonResponse


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

from django.shortcuts import render
from .models import Post

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'posts/post_list.html', {'posts': posts})





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



