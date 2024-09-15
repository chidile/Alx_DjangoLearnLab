# blog/views.py  

from django.shortcuts import render, redirect  
from django.contrib.auth import authenticate, login, logout  
from django.contrib.auth.decorators import login_required  
from .forms import RegistrationForm,PostForm, CommentForm
from django.views import generic  
from django.urls import reverse_lazy  
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin   
from .models import Post, Comment

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
 

class IsAuthorMixin(UserPassesTestMixin):  
    def test_func(self):  
        post = self.get_object()  
        return self.request.user == post.author   

class PostListView(generic.ListView):  
    model = Post  
    template_name = 'blog/post_list.html'  

class PostDetailView(IsAuthorMixin, generic.DetailView):  
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

class PostUpdateView( LoginRequiredMixin, generic.UpdateView):  
    model = Post  
    form_class = PostForm  
    template_name = 'blog/post_form.html'  
    success_url = reverse_lazy('post_list')  

    def get_queryset(self):  
        return Post.objects.filter(author=self.request.user)  

class PostDeleteView(IsAuthorMixin, LoginRequiredMixin, generic.DeleteView):  
    model = Post  
    template_name = 'blog/post_confirm_delete.html'  
    success_url = reverse_lazy('post_list')  

    def get_queryset(self):  
        return Post.objects.filter(author=self.request.user)   

class CommentListView(generic.ListView):  
    model = Comment  
    template_name = 'blog/comment_list.html'  
    
    def get_queryset(self):  
        return Comment.objects.filter(post=self.kwargs['pk'])  

class CommentCreateView(LoginRequiredMixin, generic.CreateView):  
    model = Comment  
    form_class = CommentForm  
    template_name = 'blog/comment_form.html'  

    def form_valid(self, form):  
        form.instance.post_id = self.kwargs['post_id']  
        form.instance.author = self.request.user  
        return super().form_valid(form)  

class CommentUpdateView(LoginRequiredMixin, generic.UpdateView):  
    model = Comment  
    form_class = CommentForm  
    template_name = 'blog/comment_form.html'  

    def get_queryset(self):  
        return Comment.objects.filter(author=self.request.user)  

class CommentDeleteView(LoginRequiredMixin, generic.DeleteView):  
    model = Comment  
    template_name = 'blog/comment_confirm_delete.html'  

    def get_queryset(self):  
        return Comment.objects.filter(author=self.request.user)  

    def get_success_url(self):  
        return self.object.post.get_absolute_url() 