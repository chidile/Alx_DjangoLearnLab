from django.shortcuts import render

# api/views.py  

from rest_framework import generics,viewsets
from .models import Book  
from .serializers import BookSerializer  
from rest_framework.authtoken.views import ObtainAuthToken  
from rest_framework.authtoken.models import Token  
from rest_framework.response import Response  
from rest_framework import status  

class BookListCreate(generics.ListCreateAPIView):  
    queryset = Book.objects.all()  # Retrieve all Book instances
    serializer_class = BookSerializer   # Use the BookSerializer for serialization 
  

class BookList(generics.ListAPIView):  
    queryset = Book.objects.all()  # Retrieve all Book instances  
    serializer_class = BookSerializer  # Use the BookSerializer for serialization



class BookViewSet(viewsets.ModelViewSet):  
    queryset = Book.objects.all()  # Retrieve all Book instances  
    serializer_class = BookSerializer  # Use the BookSerializer for serialization


class CustomAuthToken(ObtainAuthToken):  
    def post(self, request, *args, **kwargs):  
        serializer = self.serializer_class(data=request.data)  
        if serializer.is_valid():  
            user = serializer.validated_data['user']  
            token, created = Token.objects.get_or_create(user=user)  
            return Response({'token': token.key}, status=status.HTTP_200_OK)  
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)