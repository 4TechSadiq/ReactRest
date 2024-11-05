from django.shortcuts import render
from rest_framework import generics
from .models import Books,Students, Catalog, Provide, Admin
from .serializers import BooksSerializer,StudentsSerializer, CatelogSerializer, AdminSerializer, ProvideSerializer
from rest_framework.permissions import AllowAny
from .models import Admin
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Provide
from .serializers import ProvideSerializer
from .ImageUrl import get_url

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


class DetailBookView(generics.RetrieveAPIView):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer
    

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


class CreateAdmin(generics.ListCreateAPIView):
    queryset = Admin.objects.all()
    serializer_class = AdminSerializer


class NewCatelog(generics.ListCreateAPIView):
    queryset = Catalog.objects.all()
    serializer_class = CatelogSerializer

class ListCatelog(generics.ListAPIView):
    queryset = Catalog.objects.all()
    serializer_class = CatelogSerializer

class UpdateCatelog(generics.UpdateAPIView):
    queryset = Catalog.objects.all()
    serializer_class = CatelogSerializer
    permission_classes = [AllowAny]

class DeleteCatelog(generics.DestroyAPIView):
    queryset = Catalog.objects.all()
    serializer_class = CatelogSerializer
    permission_classes = [AllowAny]


class ListAdmin(generics.ListAPIView):
    queryset = Admin.objects.all()
    serializer_class = AdminSerializer

class ProvideBook(generics.ListCreateAPIView):
    queryset = Provide.objects.all()
    serializer_class = ProvideSerializer

class ListProvide(generics.ListAPIView):
    queryset = Provide.objects.all()
    serializer_class = ProvideSerializer

class UpdateProvide(generics.UpdateAPIView):
    queryset = Provide.objects.all()
    serializer_class = ProvideSerializer
    permission_classes = [AllowAny]

class DeleteProvide(generics.DestroyAPIView):
    queryset = Provide.objects.all()
    serializer_class = ProvideSerializer
    permission_classes = [AllowAny]


# @api_view(['POST'])
# def provide_book(request):
#     print(request.data)
#     if request.method == 'POST':
#         serializer = ProvideSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Provide
from .serializers import ProvideSerializer

class ProvideUpdateView(APIView):
    def put(self, request, pk):
        print(request.data)
        try:
            provide_instance = Provide.objects.get(pk=pk)
        except Provide.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = ProvideSerializer(provide_instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AddBook(APIView):
    def post(self, request):
        
        post_request = request.data
        print(post_request)
        url = get_url(post_request['image'])
        print(url)
        post_request['image'] = url
        serializer = BooksSerializer(data=post_request)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class CreateUser(APIView):
    def post(self, request):
        post_request = request.data
        print(post_request)
        url = get_url(post_request['profile'])
        print(url)
        post_request['profile'] = url
        serializer = StudentsSerializer(data=post_request)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)