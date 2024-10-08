from relationship_app.models import Author, Book, Library, Librarian  

# Query all books by a specific author  
author = Author.objects.get(name=author_name)  # Replace '1' with the author's ID you want  
books_by_author = Book.objects.filter(author=author)  

# List all books in a library  
specific_library = Library.objects.get(name=library_name)   
books_in_library = specific_library.books.all()  

# Retrieve the librarian for a library  
librarian_for_library = Librarian.objects.get(library=specific_library)