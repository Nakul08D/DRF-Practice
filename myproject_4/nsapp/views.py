from rest_framework import serializers
from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer
from rest_framework import generics

# Create your views here.

class AuthorList(generics.ListCreateAPIView):
    queryset=Author.objects.all()
    serializer_class=AuthorSerializer
    
class AuthorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Author.objects.all()
    serializer_class=AuthorSerializer
    
    
class BookList(generics.ListCreateAPIView):
    queryset=Book.objects.all()
    serializer_class=BookSerializer
    

class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Book.objects.all()
    serializer_class=BookSerializer

    