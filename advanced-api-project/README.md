# Book API Documentation  

## Endpoints  

- **GET /books/**: Retrieve a list of all books.  
- **GET /books/<int:pk>/**: Retrieve a specific book by ID.  
- **POST /books/create/**: Add a new book (authenticated users only).  
- **PUT /books/update/<int:pk>/**: Update an existing book (authenticated users only).  
- **DELETE /books/delete/<int:pk>/**: Remove a book (authenticated users only).  

## Permissions  

- List and Detail views are accessible to all users.  
- Create, Update, and Delete views require authentication.


class BookListView(generics.ListAPIView):  
    """  
    API view to retrieve a list of books.  
    
    Filtering options:  
    - Filter by title: ?title=<title>  
    - Filter by author: ?author__name=<author_name>  
    - Filter by publication year: ?publication_year=<year>  

    Searching options:  
    - Search by title and author name: ?search=<search_term>  

    Ordering:  
    - Order by title: ?ordering=title  
    - Order by publication year: ?ordering=publication_year  
    """  
    ...