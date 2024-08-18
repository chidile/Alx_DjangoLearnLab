from django.urls import path  
from django.contrib.auth import views as auth_views 
from . import views
from .views import list_books 
from .views import register, login_view, LogoutView  

urlpatterns = [  
    path('books/', list_books, name='list_books'),  
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),  
    path('register/', views.register, name='register'),  
    path('login/', login_view, name='login'),  
    path('logout/', LogoutView.as_view(template_name="logout")), 
]