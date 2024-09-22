
from rest_framework import viewsets, permissions, generics,status
from .models import Post, Comment, Post, Like 
from .serializers import PostSerializer, CommentSerializer 
from notifications.models import Notification  
from django.shortcuts import get_object_or_404   
from rest_framework.response import Response
from notifications.models import Notification  


class PostViewSet(viewsets.ModelViewSet):  
    queryset = Post.objects.all()  
    serializer_class = PostSerializer  
    permission_classes = [permissions.IsAuthenticated] 
    

    def perform_create(self, serializer):  
        serializer.save(author=self.request.user)  

    def perform_update(self, serializer):  
        post = self.get_object()  
        if post.author != self.request.user:  
            raise permissions.PermissionDenied("You do not have permission to edit this post.")  
        serializer.save()  

    def perform_destroy(self, serializer):  
        post = self.get_object()  
        if post.author != self.request.user:  
            raise permissions.PermissionDenied("You do not have permission to delete this post.")  
        post.delete()  

class CommentViewSet(viewsets.ModelViewSet):  
    queryset = Comment.objects.all()  
    serializer_class = CommentSerializer  
    permission_classes = [permissions.IsAuthenticated]  

    def perform_create(self, serializer):  
        serializer.save(author=self.request.user)  

    def perform_update(self, serializer):  
        comment = self.get_object()  
        if comment.author != self.request.user:  
            raise permissions.PermissionDenied("You do not have permission to edit this comment.")  
        serializer.save()  

    def perform_destroy(self, serializer):  
        comment = self.get_object()  
        if comment.author != self.request.user:  
            raise permissions.PermissionDenied("You do not have permission to delete this comment.")  
        comment.delete()


class FeedView(generics.ListAPIView):  
    serializer_class = PostSerializer  
    permission_classes = [permissions.IsAuthenticated]  

    def get_queryset(self):  
        user = self.request.user  
        following_users = user.following.all()  
        return Post.objects.filter(author__in=following_users).order_by('-created_at')  
    


class LikePostView(generics.CreateAPIView):  
    permission_classes = [permissions.IsAuthenticated]  

    def post(self, request, pk):  
        post = generics.get_object_or_404(Post, pk=pk)  
        like, created = Like.objects.get_or_create(user=request.user, post=post)  

        if not created:  
            return Response({'error': 'You have already liked this post.'}, status=status.HTTP_400_BAD_REQUEST)  

        # Create a notification  
        Notification.objects.create(  
            recipient=post.author,  
            actor=request.user,  
            verb='liked your post',  
            target_content_type=ContentType.objects.get_for_model(Post),  
            target_object_id=post.id,  
        )  
        return Response({'status': 'liked'}, status=status.HTTP_201_CREATED)  

class UnlikePostView(generics.DestroyAPIView):  
    permission_classes = [permissions.IsAuthenticated]  

    def delete(self, request, pk):  
        post = get_object_or_404(Post, pk=pk)  
        try:  
            like = Like.objects.get(post=post, user=request.user)  
            like.delete()  
            return Response({'status': 'unliked'}, status=status.HTTP_204_NO_CONTENT)  
        except Like.DoesNotExist:  
            return Response({'error': 'You have not liked this post.'}, status=status.HTTP_400_BAD_REQUEST)