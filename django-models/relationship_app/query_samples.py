from relationship_app.models import Author, Book, Library, Librarian  

# Query all books by a specific author  
specific_author = Author.objects.get(id=1)  # Replace '1' with the author's ID you want  
books_by_author = Book.objects.filter(author=specific_author)  

# List all books in a library  
library_name = Library.objects.get(id=1)  # Replace '1' with the library's ID you want  
books_in_library = library_name.books.all()  

# Retrieve the librarian for a library  
librarian_for_library = Librarian.objects.get(name=library_name)