from django.urls import path  
from django.contrib.auth import views as auth_views 
from . import views

from .views import list_books 
from .views import LoginView, LogoutView  

from .views import admin_view, librarian_view, member_view 

from .views import add_book, edit_book, delete_book

from django.conf import settings  
from django.conf.urls.static import static  


urlpatterns = [  
    path('books/', list_books, name='list_books'),  
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'), 

    path('register/', views.register, name='register'),  
    path('login/', LoginView.as_view(template_name="login"), name='login'),  
    path('logout/', LogoutView.as_view(template_name="logout"), name="logout"), 

    path('admin/', admin_view, name='admin_view'),  
    path('librarian/', librarian_view, name='librarian_view'),  
    path('member/', member_view, name='member_view'),

    path('books/add_book/', add_book, name='add_book'),  
    path('books/edit_book/<int:book_id>/', edit_book, name='edit_book'),  
    path('books/delete/<int:book_id>/', delete_book, name='delete_book'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)