# urls.py  

from django.urls import path  
from .views import secure_view, success_view  

urlpatterns = [  
    path('secure/', secure_view, name='secure_view'),  
    path('success/', success_view, name='success_view'),  
]