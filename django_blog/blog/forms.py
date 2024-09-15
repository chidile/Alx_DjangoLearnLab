

from django import forms  
from django.contrib.auth.forms import UserCreationForm  
from django.contrib.auth.models import User  
from .models import Post, Comment
from taggit.forms import TagField, TagWidget

class RegistrationForm(UserCreationForm):  
    email = forms.EmailField(required=True)  

    class Meta:  
        model = User  
        fields = ['username', 'email', 'password1', 'password2']


class PostForm(forms.ModelForm): 
    tags = TagField(widgets=TagWidget(attrs={'placeholder': 'Add tags, separated by commas'}))  # Use TagWidget

    class Meta:  
        model = Post  
        fields = ['title', 'content',  'tags']  

class CommentForm(forms.ModelForm):  
    class Meta:  
        model = Comment  
        fields = ['content'] 

posts_with_tag = Post.objects.filter(tags__name__in=['tag_name']) 