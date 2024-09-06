from rest_framework import generics  
from .models import Book  
from .serializers import BookSerializer  
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated  
from rest_framework import filters  
from django_filters.rest_framework import DjangoFilterBackend  


class BookListView(generics.ListAPIView):  
    queryset = Book.objects.all()  
    serializer_class = BookSerializer  
    permission_classes = [IsAuthenticatedOrReadOnly] 
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]  
    filterset_fields = ['title', 'author', 'publication_year']  
    search_fields = ['title', 'author']   
    ordering_fields = ['title', 'publication_year']  
    ordering = ['title']

class BookDetailView(generics.RetrieveAPIView):  
    queryset = Book.objects.all()  
    serializer_class = BookSerializer  
    permission_classes = [IsAuthenticatedOrReadOnly]  

class BookCreateView(generics.CreateAPIView):  
    queryset = Book.objects.all()  
    serializer_class = BookSerializer  
    permission_classes = [IsAuthenticated]  

class BookUpdateView(generics.UpdateAPIView):  
    queryset = Book.objects.all()  
    serializer_class = BookSerializer  
    permission_classes = [IsAuthenticated]  

class BookDeleteView(generics.DestroyAPIView):  
    queryset = Book.objects.all()  
    serializer_class = BookSerializer  
    permission_classes = [IsAuthenticated]