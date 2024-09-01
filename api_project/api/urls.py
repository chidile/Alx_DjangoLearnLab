# api/urls.py  

from django.urls import path  
from .views import BookListCreate, BookList 

urlpatterns = [  
    path('books/', BookListCreate.as_view(), name='book-list-create'), 
    path('books/', BookList.as_view(), name='book-list'),  # Route to the BookList view  
]