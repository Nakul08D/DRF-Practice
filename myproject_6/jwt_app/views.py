from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from .serializers import UserSerializer
from django.contrib.auth import authenticate
from rest_framework.decorators import permission_classes,authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.contrib.auth.hashers import make_password

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

class RegistrationAPIView(APIView):
    def get(self, request):
        try:
            user=User.objects.all()
            serializer=UserSerializer(user, many=True)
            context ={
                'success':True,
                "status": status.HTTP_200_OK,
                "data":serializer.data
            }
            return Response(context)
        except:
            context ={
                'success':False,
                "status": status.HTTP_204_NO_CONTENT,
                "data":serializer.data
            }
            return Response(context)
    
    def post(self, request):
        try:
            serializer=UserSerializer(data=request.data)
            if serializer.is_valid():
                user=serializer.save(password=make_password(request.data.get("password")))
                token=get_tokens_for_user(user)
                context={
                    "success":True,
                    "status": status.HTTP_201_CREATED,
                    "token":token,
                    "data":serializer.data
                }
            return Response(context)
        except:
            context={
                    "success":False,
                    "status": status.HTTP_501_NOT_IMPLEMENTED,
                    "data":serializer.data
                }
            return Response(context)
        
class RegistrationDetailAPIView(APIView):
    def get(self, request, pk):
        try:
            user=User.objects.get(pk=pk)
            serializer=UserSerializer(user)
            context ={
                'success':True,
                "status": status.HTTP_200_OK,
                "data":serializer.data
            }
            return Response(context)
        except:
            context ={
                'success':False,
                "status": status.HTTP_204_NO_CONTENT,
                "data":serializer.data
            }
            return Response(context)
    
    def put(self, request,pk):
        try:
            user=User.objects.get(pk=pk)
            serializer=UserSerializer(user,data=request.data)
            if serializer.is_valid():
                serializer.save()
                context={
                    "success":True,
                    "status": status.HTTP_201_CREATED,
                    "data":serializer.data
                }
            return Response(context)
        except:
            context={
                    "success":False,
                    "status": status.HTTP_501_NOT_IMPLEMENTED,
                    "data":serializer.data
                }
            return Response(context)
        
        
@authentication_classes([JWTAuthentication])  
@permission_classes([IsAuthenticated]) 
class LoginDetail(APIView):
    def post(self,request):
        try:
            data=request.data
            username=data.get('username')
            password=data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                # token=get_tokens_for_user(user)
                context={
                    "success":True,
                    "status": status.HTTP_302_FOUND,
                    "msg":"logIn"
                }
                return Response(context)
            else:
                return Response({"msg":"Not_logeIn"})
        except:
            return Response({"msg":"Invalid Creaditionals"})
                    