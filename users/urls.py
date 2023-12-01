from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('create_profile/', views.create_profile, name='create_profile'),
    path('<str:username>/follow/', views.follow_user, name='follow_user'),
    path('<str:username>/unfollow/', views.unfollow_user, name='unfollow_user'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('signup/', views.user_signup, name='signup'),
]