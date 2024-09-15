

from django import forms  
from django.contrib.auth.forms import UserCreationForm  
from django.contrib.auth.models import User  
from .models import Post, Comment, Tag 

class RegistrationForm(UserCreationForm):  
    email = forms.EmailField(required=True)  

    class Meta:  
        model = User  
        fields = ['username', 'email', 'password1', 'password2']


class PostForm(forms.ModelForm):  
    class Meta:  
        model = Post  
        fields = ['title', 'content',  'tags']  
    
    def __init__(self, *args, **kwargs):  
        super(PostForm, self).__init__(*args, **kwargs)  
        self.fields['tags'].queryset = Tag.objects.all()  

class CommentForm(forms.ModelForm):  
    class Meta:  
        model = Comment  
        fields = ['content'] 