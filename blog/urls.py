from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('register.html/', views.register, name='new_user'),
    path('login.html/', views.log_in, name='log_in'),
    path('logout.html/', views.log_out, name='log_out'),
    path('post/profile.html/<str:au>', views.user_profile, name='user_profile'),
    path('posts.html/<str:au>', views.user_posts, name='user_posts'),
]
