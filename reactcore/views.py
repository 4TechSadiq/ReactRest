from django.shortcuts import render
from rest_framework import generics
from .models import Books
from .serializers import BooksSerializer,StudentsSerializer
# Create your views here.

class BooksList(generics.ListCreateAPIView):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer