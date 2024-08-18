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