from django.shortcuts import render  
from .models import Book
from django.views.generic.detail import DetailView 
from .models import Library 

from django.contrib.auth import login, authenticate  
from django.contrib.auth.forms import UserCreationForm  
from django.shortcuts import render, redirect  
from django.contrib.auth.views import LogoutView 
from django.contrib.auth.views import LoginView  
from django.urls import reverse_lazy 

def list_books(request):  
    books = Book.objects.all()  
    context = {'books': books}  
    return render(request, 'relationship_app/list_books.html', context)

class LibraryDetailView(DetailView):  
    model = Library  
    template_name = 'relationship_app/library_detail.html'


# Registration View  
def register(request):  
    if request.method == 'POST':  
        form = UserCreationForm(request.POST)  
        if form.is_valid():  
            user = form.save()  
            login(request, user)  # Log the user in right after registration  
            return redirect('list_books')  # Redirect to a page after registration  
    else:  
        form = UserCreationForm()  
    return render(request, 'relationship_app/register.html', {'form': form})  

# Login View  
class CustomLoginView(LoginView):  
    template_name = 'relationship_app/login.html'  # Specify your login template  
    success_url = reverse_lazy('list_books') 

# Logout View (using built-in LogoutView)  
class LogoutView(LogoutView):  
    template_name = 'relationship_app/logout.html' 

from django.contrib.auth.decorators import user_passes_test  
from django.shortcuts import render  

def is_admin(user):  
    return user.userprofile.role == 'Admin'  

def is_librarian(user):  
    return user.userprofile.role == 'Librarian'  

def is_member(user):  
    return user.userprofile.role == 'Member'  

@user_passes_test(is_admin)  
def admin_view(request):  
    return render(request, 'admin_view.html')  

@user_passes_test(is_librarian)  
def librarian_view(request):  
    return render(request, 'librarian_view.html')  

@user_passes_test(is_member)  
def member_view(request):  
    return render(request, 'member_view.html')




from django.contrib.auth.decorators import permission_required  

@permission_required('relationship_app.can_add_book')  
def add_book(request):  
    # Logic to add book...  
    pass

@permission_required('relationship_app.can_change_book')  
def edit_book(request, book_id):  
    # Logic to edit book...  
    pass

@permission_required('relationship_app.can_delete_book')  
def delete_book(request, book_id):  
    # Logic to delete book...
    pass

    