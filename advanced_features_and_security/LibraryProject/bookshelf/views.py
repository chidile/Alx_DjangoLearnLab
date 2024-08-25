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