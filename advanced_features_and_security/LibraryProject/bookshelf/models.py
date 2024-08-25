from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager 



class Book(models.Model):  
    title = models.CharField(max_length=200)  
    author = models.CharField(max_length=100)  
    publication_year = models.IntegerField()  

    def __str__(self):  
        return self.title 


 