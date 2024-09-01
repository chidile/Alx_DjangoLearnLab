from django.shortcuts import render

# api/views.py  

from rest_framework import generics,viewsets
from .models import Book  
from .serializers import BookSerializer  

class BookListCreate(generics.ListCreateAPIView):  
    queryset = Book.objects.all()  # Retrieve all Book instances
    serializer_class = BookSerializer   # Use the BookSerializer for serialization 
  

class BookList(generics.ListAPIView):  
    queryset = Book.objects.all()  # Retrieve all Book instances  
    serializer_class = BookSerializer  # Use the BookSerializer for serialization



class BookViewSet(viewsets.ModelViewSet):  
    queryset = Book.objects.all()  # Retrieve all Book instances  
    serializer_class = BookSerializer  # Use the BookSerializer for serialization