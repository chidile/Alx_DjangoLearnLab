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


# Example API requests  
GET /books/?title=Example  # Filter by title  
GET /books/?search=Example  # Search by title and author  
GET /books/?ordering=title  # Order by title