## Delete the book instance  
from bookshelf.models import Book
book = Book.objects.all() 
book.delete() 
