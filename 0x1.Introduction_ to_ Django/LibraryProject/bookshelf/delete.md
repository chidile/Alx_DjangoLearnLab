## Delete the book instance  
from bookshelf.models import Book
books = Book.objects.all() 
books.delete() 