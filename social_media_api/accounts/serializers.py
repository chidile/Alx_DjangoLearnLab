from rest_framework import serializers  
from django.contrib.auth import get_user_model  
from rest_framework.authtoken.models import Token  

User = get_user_model()  




class UserSerializer(serializers.ModelSerializer):  
    class Meta:  
        model = User  
        fields = ['id', 'username', 'bio', 'profile_picture', 'followers'] 


class RegisterSerializer(serializers.ModelSerializer):  
    class Meta:  
        model = User  
        fields = ['username', 'password', 'bio', 'profile_picture'] 
        name = serializers.CharField()  

    # Create a new user  
    user = get_user_model().objects.create_user()  
    user.save() 

    def create(self, validated_data):  
        user = User(**validated_data)  
        user.set_password(validated_data['password'])  
        user.save()  
        Token.objects.create(user=user)  
        return user