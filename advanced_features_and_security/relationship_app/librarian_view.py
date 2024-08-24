from django.contrib.auth.decorators import user_passes_test  
from django.shortcuts import render  

# Check if the user is a Librarian  
def is_librarian(user):  
    return user.is_authenticated and user.role == 'Librarian'  

@user_passes_test(is_librarian)  
def librarian_view(request):  
    return render(request, 'librarian_view.html')