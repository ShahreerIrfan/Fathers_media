# posts/views.py

from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from django.http import JsonResponse
import random
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Post, Comment
from .forms import LikeForm, CommentForm


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


def post_list(request):
    all_posts = Post.objects.all()
    # random(all_posts)
    return render(request, 'posts/post_list.html', {'posts': all_posts})


def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    comments = Comment.objects.filter(post=post)

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.user = request.user  # Assuming you have user authentication
            new_comment.save()
            comments = Comment.objects.filter(post=post)  # Update comments after adding a new one


            comments_html = render(request, 'posts/comments.html', {'comments': comments}).content.decode('utf-8')

            return JsonResponse({'success': True, 'comments_html': comments_html})
        else:
            return JsonResponse({'success': False, 'errors': comment_form.errors})

    else:
        comment_form = CommentForm()

    return render(request, 'posts/post_detail.html', {'post': post, 'comments': comments, 'comment_form': comment_form})








def like_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.user in post.likes.all():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True

    return JsonResponse({'liked': liked, 'likes_count': post.likes.count})



# ..........