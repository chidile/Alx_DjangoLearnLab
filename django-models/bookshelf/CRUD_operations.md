## Create a Book instance
book = Book.objects.get(title="1984")  
print(book)

## Update the book's title  
book.title = "Nineteen Eighty-Four"  
book.save()

book = Book.objects.get(title="1984")  
print(book) 

## Delete the book instance  
from bookshelf.models import Book
books = Book.objects.all() 
books.delete() 


