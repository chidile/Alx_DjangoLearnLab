from django.urls import path  
from . import views  
from .views import *

urlpatterns = [  
    path('register/', views.register, name='register'),  
    path('login/', views.login_view, name='login'),  
    path('logout/', views.logout_view, name='logout'),  
    path('profile/', views.profile, name='profile'),  
    path('profile/edit/', views.edit_profile, name='edit_profile'),

    path('posts/', PostListView.as_view(), name='post_list'),  
    path('post/new/', PostCreateView.as_view(), name='post_create'),  
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),  
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post_edit'),  
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),

    path('posts/<int:post_id>/comments/', CommentListView.as_view(), name='comment_list'),  
    path('post/<int:pk>/comments/new/', CommentCreateView.as_view(), name='comment_create'),  
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='comment_edit'),  
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment_delete'), 

    path('search/', search_posts, name='search_posts'),  # Add search URL  
    path('tags/<slug:tag_slug>/', PostByTagListView.as_view(), name='posts_by_tag'),  # Add search URL  
]