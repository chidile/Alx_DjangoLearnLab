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

# Testing Documentation  

## Testing Strategy  
Tests are designed to verify the functionality of the Book API endpoints, including CRUD operations, filtering, searching, and permission checks.  

## Test Cases  
1. **Create Book**: Tests the creation of a book and checks the response status and data integrity.  
2. **Update Book**: Tests updating a book's data and checks if changes are correctly reflected.  
3. **Delete Book**: Tests if a book is successfully deleted and no longer exists in the database.  
4. **Filter Books**: Tests that filtering works as expected for book titles.  
5. **Search Books**: Tests that searching across author names retrieves the correct books.  

## Running Tests  
To run the tests, execute the following command in your terminal:  
```bash  
python manage.py test api