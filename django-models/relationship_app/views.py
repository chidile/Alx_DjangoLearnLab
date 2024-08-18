from django.shortcuts import render  
from .models import Book
from django.views.generic.detail import DetailView 
from .models import Library 

from django.contrib.auth import login, authenticate  
from django.contrib.auth.forms import UserCreationForm  
from django.shortcuts import render, redirect  
from django.contrib.auth.views import LogoutView 

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
    return render(request, 'register.html', {'form': form})  

# Login View  
def login_view(request):  
    if request.method == 'POST':  
        username = request.POST['username']  
        password = request.POST['password']  
        user = authenticate(request, username=username, password=password)  
        if user is not None:  
            login(request, user)  
            return redirect('list_books')  # Redirect to a page after login  
    return render(request, 'login.html')  

# Logout View (using built-in LogoutView)  
class CustomLogoutView(LogoutView):  
    template_name = 'logout.html' 