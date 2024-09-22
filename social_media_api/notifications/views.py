# notifications/views.py  
from rest_framework import generics, permissions 
from rest_framework.response import Response 
from .models import Notification  

class NotificationListView(generics.ListAPIView):  
    permission_classes = [permissions.IsAuthenticated]  

    def get_queryset(self):  
        return Notification.objects.filter(recipient=self.request.user)  

    # Optional: Mark notifications as read  
    def mark_as_read(self, request, notification_id):  
        notification = Notification.objects.get(id=notification_id)  
        notification.is_read = True  # Assuming there is an is_read field  
        notification.save()  
        return Response({'status': 'marked as read'}, status=200)