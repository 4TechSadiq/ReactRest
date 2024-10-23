from django.urls import path
from . import views

urlpatterns = [
    path("", views.CreateBook.as_view(), name="create-book"),
    path("list", views.ListBooks.as_view(), name="list-books"),
    path("create-student", views.CreateStudent.as_view(), name="create-student"),
]
