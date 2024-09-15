# blog/views.py  

from django.shortcuts import render, redirect  
from django.contrib.auth import authenticate, login, logout  
from django.contrib.auth.decorators import login_required  
from .forms import RegistrationForm  
from django.views import generic  
from django.urls import reverse_lazy  
from django.contrib.auth.mixins import LoginRequiredMixin  
from .models import Post  
from .forms import PostForm 

def register(request):  
    if request.method == 'POST':  
        form = RegistrationForm(request.POST)  
        if form.is_valid():  
            form.save()  
            username = form.cleaned_data['username']  
            password = form.cleaned_data['password1']  
            user = authenticate(username=username, password=password)  
            login(request, user)  
            return redirect('home')  
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
            return redirect('home')   
    return render(request, 'blog/login.html')  

@login_required  
def logout_view(request):  
    logout(request)  
    return redirect('home')  

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
 

 

class PostListView(generic.ListView):  
    model = Post  
    template_name = 'blog/post_list.html'  

class PostDetailView(generic.DetailView):  
    model = Post  
    template_name = 'blog/post_detail.html'  

class PostCreateView(LoginRequiredMixin, generic.CreateView):  
    model = Post  
    form_class = PostForm  
    template_name = 'blog/post_form.html'  
    success_url = reverse_lazy('post_list')  # Adjust name accordingly  

    def form_valid(self, form):  
        form.instance.author = self.request.user  
        return super().form_valid(form)  

class PostUpdateView(LoginRequiredMixin, generic.UpdateView):  
    model = Post  
    form_class = PostForm  
    template_name = 'blog/post_form.html'  
    success_url = reverse_lazy('post_list')  

    def get_queryset(self):  
        return Post.objects.filter(author=self.request.user)  

class PostDeleteView(LoginRequiredMixin, generic.DeleteView):  
    model = Post  
    template_name = 'blog/post_confirm_delete.html'  
    success_url = reverse_lazy('post_list')  

    def get_queryset(self):  
        return Post.objects.filter(author=self.request.user)