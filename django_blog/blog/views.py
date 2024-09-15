# blog/views.py  

from django.shortcuts import render, redirect  
from django.contrib.auth import authenticate, login, logout  
from django.contrib.auth.decorators import login_required  
from .forms import RegistrationForm  

def register(request):  
    if request.method == 'POST':  
        form = RegistrationForm(request.POST)  
        if form.is_valid():  
            form.save()  
            username = form.cleaned_data['username']  
            password = form.cleaned_data['password1']  
            user = authenticate(username=username, password=password)  
            login(request, user)  
            return redirect('home')  # Change 'home' to your desired landing page  
    else:  
        form = RegistrationForm()  
    return render(request, 'blog/register.html', {'form': form})  

def login_view(request):  
    if request.method == 'POST':  
        username = request.POST['username']  
        password = request.POST['password']  
        user = authenticate(request, username=username, password=password)  
        if user is not None:  
            login(request, user)  
            return redirect('home')  # Change 'home' to your desired landing page  
    return render(request, 'blog/login.html')  

@login_required  
def logout_view(request):  
    logout(request)  
    return redirect('home')  # Change 'home' to your desired landing page  

@login_required  
def profile(request):  
    return render(request, 'blog/profile.html')  

@login_required  
def edit_profile(request):  
    if request.method == 'POST':  
        form = RegistrationForm(request.POST, instance=request.user)  
        if form.is_valid():  
            form.save()  
            return redirect('profile')  # Redirect to profile page after editing  
    else:  
        form = RegistrationForm(instance=request.user)  
    return render(request, 'blog/edit_profile.html', {'form': form})
