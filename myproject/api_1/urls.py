from django.urls import path
from api_1 import views

urlpatterns = [
    
    path('',views.home,name='home'),
    path('info/',views.info,name='info'),
    path('info/<int:id>/',views.info,name='info'),
    
    
]