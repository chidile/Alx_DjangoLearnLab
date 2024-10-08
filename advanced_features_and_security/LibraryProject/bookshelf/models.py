from django.db import models  
from django.contrib.auth.models import User 
from django.contrib.auth.models import AbstractUser

class Author(models.Model):  
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name 

class Book(models.Model):  
    title = models.CharField(max_length=100)  
    author = models.ForeignKey(Author, on_delete=models.CASCADE) 
    
    class Meta:  
        permissions = [  
            ("can_add_book", "Can add book"),  
            ("can_change_book", "Can change book"),  
            ("can_delete_book", "Can delete book"),  
        ]  

class Library(models.Model):  
    name = models.CharField(max_length=100)  
    books = models.ManyToManyField(Book)

    def __str__(self):
        return self.name   

class Librarian(models.Model):  
    name = models.CharField(max_length=100)  
    library = models.OneToOneField(Library, on_delete=models.CASCADE)
    def __str__(self):
        return self.name 


 

class UserProfile(models.Model):  
    USER_ROLES = [  
        ('Admin', 'Admin'),  
        ('Librarian', 'Librarian'),  
        ('Member', 'Member'),  
    ]  
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)  
    role = models.CharField(max_length=20, choices=USER_ROLES)  

    def __str__(self):  
        return f"{self.user.username} - {self.role}"
    

from django.db.models.signals import post_save  
from django.dispatch import receiver  

@receiver(post_save, sender=User)  
def create_user_profile(sender, instance, created, **kwargs):  
    if created:  
        UserProfile.objects.create(user=instance)





from django.contrib.auth.models import AbstractUser, BaseUserManager  

class MyModel(models.Model):  
    name = models.CharField(max_length=100)  

    class Meta:  
        permissions = [  
            ('can_view', 'Can view model'),  
            ('can_create', 'Can create model'),  
            ('can_edit', 'Can edit model'),  
            ('can_delete', 'Can delete model'),  
        ]

class CustomUserManager(BaseUserManager):  
    def create_user(self, username, password=None, **extra_fields):  
        if not username:  
            raise ValueError("The Username field must be set")  
        user = self.model(username=username, **extra_fields)  
        user.set_password(password)  # Hash the password  
        user.save(using=self._db)  
        return user  

    def create_superuser(self, username, password=None, **extra_fields):  
        extra_fields.setdefault('is_staff', True)  
        extra_fields.setdefault('is_superuser', True)  

        if extra_fields.get('is_staff') is not True:  
            raise ValueError("Superuser must have is_staff=True.")  
        if extra_fields.get('is_superuser') is not True:  
            raise ValueError("Superuser must have is_superuser=True.")  

        return self.create_user(username, password, **extra_fields)  

class CustomUser(AbstractUser):  
    date_of_birth = models.DateField(null=True, blank=True)  
    profile_photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)  

    objects = CustomUserManager()