from django.shortcuts import render
from rest_framework import generics
from .models import Books,Students
from .serializers import BooksSerializer,StudentsSerializer
from rest_framework.permissions import AllowAny
# Create your views here.

class CreateBook(generics.ListCreateAPIView):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer

class ListBooks(generics.ListAPIView):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer

class UpdateBook(generics.UpdateAPIView):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer
    permission_classes = [AllowAny]

class DeleteBook(generics.DestroyAPIView):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer
    permission_classes = [AllowAny]
    




class CreateStudent(generics.ListCreateAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentsSerializer
