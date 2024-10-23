from django.shortcuts import render
from rest_framework import generics
from .models import Books,Students, Catelog
from .serializers import BooksSerializer,StudentsSerializer, CatelogSerializer
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

class ListStudent(generics.ListAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentsSerializer

class UpdateStudent(generics.UpdateAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentsSerializer
    permission_classes = [AllowAny]

class DeleteStudent(generics.DestroyAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentsSerializer
    permission_classes = [AllowAny]



class NewCatelog(generics.ListCreateAPIView):
    queryset = Catelog.objects.all()
    serializer_class = CatelogSerializer

class ListCatelog(generics.ListAPIView):
    queryset = Catelog.objects.all()
    serializer_class = CatelogSerializer

class UpdateCatelog(generics.UpdateAPIView):
    queryset = Catelog.objects.all()
    serializer_class = CatelogSerializer
    permission_classes = [AllowAny]

class DeleteCatelog(generics.DestroyAPIView):
    queryset = Catelog.objects.all()
    serializer_class = CatelogSerializer
    permission_classes = [AllowAny]