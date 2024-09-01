# api/urls.py  

from django.urls import path,include
from .views import BookListCreate, BookList, BookViewSet 
from rest_framework.routers import DefaultRouter  

router = DefaultRouter()  
router.register(r'books', BookViewSet)  # Register the BookViewSet with the router 
urlpatterns = [  
    path('books/', BookListCreate.as_view(), name='book-list-create'), 
    path('books/', BookList.as_view(), name='book-list'),  # Route to the BookList view  
    
    path('', include(router.urls)),  # Include the router URLs
]

# api/urls.py  

