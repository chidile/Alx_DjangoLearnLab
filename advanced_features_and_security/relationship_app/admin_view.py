from django.contrib.auth.decorators import user_passes_test  
from django.shortcuts import render  

# Check if the user is an Admin  
def is_admin(user):  
    return user.is_authenticated and user.role == 'Admin'  

@user_passes_test(is_admin)  
def admin_view(request):  
    return render(request, 'admin_view.html')