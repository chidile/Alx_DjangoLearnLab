from rest_framework import generics  
from rest_framework.authtoken.views import ObtainAuthToken  
from rest_framework.authtoken.models import Token  
from rest_framework.response import Response  
from .models import CustomUser  
from .serializers import UserSerializer, RegisterSerializer  

class RegisterView(generics.CreateAPIView):  
    queryset = CustomUser.objects.all()  
    serializer_class = RegisterSerializer  

class LoginView(ObtainAuthToken):  
    def post(self, request, *args, **kwargs):  
        response = super(LoginView, self).post(request, *args, **kwargs)  
        token = Token.objects.get(user=response.data['user'])  
        return Response({'token': token.key})  

class UserProfileView(generics.RetrieveUpdateAPIView):  
    queryset = CustomUser.objects.all()  
    serializer_class = UserSerializer  
    lookup_field = 'username'