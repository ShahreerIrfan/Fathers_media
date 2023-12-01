from collections import UserDict, UserList
from django.shortcuts import render, redirect
from .forms import RegistrationForm, UserProfileForm
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from .models import Follow, UserProfile
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

# Create your views here.
def home(request):
    return render(request,'users/index.html')


def user_signup(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Account created successfully. You are now logged in.')
            return redirect('home')  # Change 'home' to the name of your home page URL
    else:
        form = RegistrationForm()

    return render(request, 'users/signup.html', {'form': form})



# users/views.py



def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'You have successfully logged in.')
            return redirect('home')  # Change 'home' to the name of your home page URL
        else:
            messages.error(request, 'Invalid login credentials.')

    return render(request, 'users/login.html')

# @login_required
def user_logout(request):
    logout(request)
    messages.success(request, 'You have successfully logged out.')
    return redirect('home')  # Change 'home' to the name of your home page URL


# @login_required
def create_profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES)
        if form.is_valid():
            # Save the form data to the user's profile
            user_profile = form.save(commit=False)
            user_profile.user = request.user
            user_profile.save()
            # return redirect('profile')  # Redirect to the user's profile page
    else:
        form = UserProfileForm()

    return render(request, 'users/create_profile.html', {'form': form})


# @login_required
def follow_user(request, username):
    user_to_follow = get_object_or_404(UserList, username=username)
    
    if user_to_follow == request.user:
        messages.warning(request, "You can't follow yourself.")
    else:
        Follow.objects.get_or_create(follower=request.user, following=user_to_follow)
        messages.success(request, f"You are now following {user_to_follow.username}.")

    return redirect('profile', username=username)

# @login_required
def unfollow_user(request, username):
    user_to_unfollow = get_object_or_404(UserDict, username=username)
    
    Follow.objects.filter(follower=request.user, following=user_to_unfollow).delete()
    messages.success(request, f"You have unfollowed {user_to_unfollow.username}.")
    return redirect('profile', username=username)

