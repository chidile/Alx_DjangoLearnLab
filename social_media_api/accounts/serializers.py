from rest_framework import serializers  
from django.contrib.auth import get_user_model  
from rest_framework.authtoken.models import Token  

User = get_user_model()  

# Create a new user  
user = User.objects.create_user(  
    username='john_doe',  
    email='john@example.com',  
    password='secure_password123'  
)  
user.save()


class UserSerializer(serializers.ModelSerializer):  
    class Meta:  
        model = User  
        fields = ['id', 'username', 'bio', 'profile_picture', 'followers'] 

    def create(self, validated_data):
        return super().create(validated_data) 

class RegisterSerializer(serializers.ModelSerializer):  
    class Meta:  
        model = User  
        fields = ['username', 'password', 'bio', 'profile_picture'] 
        name = serializers.CharField(max_length=100, required=True)   

    def create(self, validated_data):  
        user = User(**validated_data)  
        user.set_password(validated_data['password'])  
        user.save()  
        Token.objects.create(user=user)  
        return user