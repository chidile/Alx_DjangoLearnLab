from rest_framework import generics  
from rest_framework.authtoken.views import ObtainAuthToken  
from rest_framework.authtoken.models import Token  
from rest_framework.response import Response  
from .models import CustomUser  
from .serializers import UserSerializer, RegisterSerializer 
from rest_framework import viewsets, permissions, status 

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



class UserViewSet(generics.GenericAPIView):  
    queryset = CustomUser.objects.all()  
    serializer_class = UserSerializer  
    permission_classes = [permissions.IsAuthenticated]  

    def follow_user(self, request, pk=None):  
        user_to_follow = self.get_object(pk)  
        request.user.following.add(user_to_follow)  
        return Response({'status': 'following'}, status=status.HTTP_200_OK)  

    def unfollow_user(self, request, pk=None):  
        user_to_unfollow = self.get_object(pk)  
        request.user.following.remove(user_to_unfollow)  
        return Response({'status': 'unfollowed'}, status=status.HTTP_200_OK)