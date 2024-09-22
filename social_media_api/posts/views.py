
from rest_framework import viewsets, permissions  
from .models import Post, Comment  
from .serializers import PostSerializer, CommentSerializer  

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