from django.shortcuts import render
from rest_framework import generics
from .models import Books
from .serializers import BooksSerializer,StudentsSerializer
# Create your views here.

class CreateBook(generics.ListCreateAPIView):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer

class ListBooks(generics.ListAPIView):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer

class CreateStudent(generics.ListCreateAPIView):
    queryset = Books.objects.all()
    serializer_class = StudentsSerializer
