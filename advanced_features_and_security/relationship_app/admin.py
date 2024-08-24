from django.contrib import admin
from . import models

# Register your models here.
admin.register(models.Librarian)



# register the customUser and customUserAdmin
from django.contrib.auth.admin import UserAdmin  
from .models import CustomUser  

class CustomUserAdmin(UserAdmin):  
    model = CustomUser  
    fieldsets = UserAdmin.fieldsets + (  
        (None, {'fields': ('date_of_birth', 'profile_photo')}),  
    )  
    add_fieldsets = UserAdmin.add_fieldsets + (  
        (None, {'fields': ('date_of_birth', 'profile_photo')}),  
    )  

admin.site.register(CustomUser, CustomUserAdmin)