from django.contrib.auth.decorators import user_passes_test  
from django.shortcuts import render  

# Check if the user is a Member  
def is_member(user):  
    return user.is_authenticated and user.role == 'Member'  

@user_passes_test(is_member)  
def member_view(request):  
    return render(request, 'member_view.html')