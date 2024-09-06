# api/test_views.py  

from rest_framework import status  
from rest_framework.test import APITestCase  
from .models import Book, Author  

class BookAPITests(APITestCase):  
    def setUp(self):  
        # Create a sample author  
        self.author = Author.objects.create(name="Sample Author") 
        # Sample book data  
        self.book_data = {  
            'title': 'Sample Book',  
            'publication_year': 2023,  
            'author': self.author.id
        }  
        # Create a book instance  
        self.book = Book.objects.create(**self.book_data)  

    def test_create_book(self):  
        response = self.client.post('/api/books/', self.book_data)  
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)  
        self.assertEqual(Book.objects.count(), 2)  # Verify book count  
        self.assertEqual(Book.objects.last().title, 'Sample Book')  

    def test_update_book(self):  
        update_data = {'title': 'Updated Book Title'}  
        response = self.client.patch(f'/api/books/{self.book.id}/', update_data)  
        self.assertEqual(response.status_code, status.HTTP_200_OK)  
        self.book.refresh_from_db()  
        self.assertEqual(self.book.title, 'Updated Book Title')  

    def test_delete_book(self):  
        response = self.client.delete(f'/api/books/{self.book.id}/')  
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)  
        self.assertFalse(Book.objects.filter(id=self.book.id).exists())  

    def test_filter_books(self):  
        response = self.client.get('/api/books/?title=Sample Book')  
        self.assertEqual(response.status_code, status.HTTP_200_OK)  
        self.assertEqual(len(response.data), 1)  

    def test_search_books(self):  
        response = self.client.get('/api/books/?search=Sample Author')  
        self.assertEqual(response.status_code, status.HTTP_200_OK)  
        self.assertGreaterEqual(len(response.data), 1)  

    def test_permission_required(self):  
        # Assuming you have a permission setup, test unauthorized access  
        response = self.client.get('/api/books/')  
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)  # Adjust based on your permission setup
    
    def test_login_required(self):  
        # Assuming you have a permission setup, test unauthorized access  
        response = self.client.login('/login/')  
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)  # Adjust based on your permission setup



        