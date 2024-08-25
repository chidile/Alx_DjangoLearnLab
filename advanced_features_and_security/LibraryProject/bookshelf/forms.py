from django import forms  

class ExampleForm(forms.Form):  
    user_input = forms.CharField(max_length=100)