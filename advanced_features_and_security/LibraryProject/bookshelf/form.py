from django import forms  

class MyForm(forms.Form):  
    user_input = forms.CharField(max_length=100)