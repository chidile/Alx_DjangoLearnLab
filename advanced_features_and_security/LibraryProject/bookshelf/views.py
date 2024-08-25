from django.shortcuts import render
from django.shortcuts import render, get_object_or_404  
from django.contrib.auth.decorators import permission_required  
from .models import   MyModel

@permission_required('app_name.can_view', raise_exception=True)  
def list_view(request):  
    book_list = MyModel.objects.all()  
    return render(request, 'list.html', {'book_list': book_list})  

@permission_required('app_name.can_create', raise_exception=True)  
def create_view(request):  
    if request.method == 'POST':  
        # Logic to create a new MyModel instance  
        pass  
    return render(request, 'create.html')  

@permission_required('app_name.can_edit', raise_exception=True)  
def edit_view(request, pk):  
    books = get_object_or_404(MyModel, pk=pk)  
    if request.method == 'POST':  
        # Logic to edit the MyModel instance  
        pass  
    return render(request, 'edit.html', {'books': books})  

@permission_required('app_name.can_delete', raise_exception=True)  
def delete_view(request, pk):  
    obj = get_object_or_404(MyModel, pk=pk)  
    if request.method == 'POST':  
        obj.delete()  
        # Redirect after deletion  
    return render(request, 'delete.html', {'object': obj})








from django.shortcuts import render, redirect  
from django.http import HttpResponse  
from django import forms  
from .models import MyModel  # Assuming you have a model named MyModel  

# Form for user input  
class MyForm(forms.Form):  
    user_input = forms.CharField(max_length=100)  

def secure_view(request):  
    if request.method == 'POST':  
        form = MyForm(request.POST)  
        if form.is_valid():  
            # Safely handle user input  
            user_input = form.cleaned_data['user_input']  
            # Use Django ORM to interact with the database  
            MyModel.objects.create(name=user_input)  
            return redirect('success_view')  # Redirect after successful creation  
    else:  
        form = MyForm()  
    return render(request, 'secure_template.html', {'form': form})  

def success_view(request):  
    return HttpResponse("Data submitted successfully!")