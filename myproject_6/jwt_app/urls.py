
from django.urls import path
from .views import RegistrationAPIView, RegistrationDetailAPIView, LoginDetail
from rest_framework_simplejwt.views import TokenVerifyView

urlpatterns = [
    
    path('registration/',RegistrationAPIView.as_view(),name='registration'),
    path('registration/<int:pk>/',RegistrationDetailAPIView.as_view(),name='registrationDetail'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('login/', LoginDetail.as_view(), name=''),
    
    
]
