from django.urls import path
from . import views

urlpatterns = [
    path("create-book/", views.CreateBook.as_view(), name="create-book"),
    path("update-book/<int:pk>", views.UpdateBook.as_view(), name="update-book"),
    path("list-book/", views.ListBooks.as_view(), name="list-books"),
    path("delete-book/", views.DeleteBook.as_view(), name="delete-book"),

    path("create-student/", views.CreateStudent.as_view(), name="create-student"),
    path("update-student/<int:pk>/", views.UpdateStudent.as_view(), name="update-student"),
    path("list-student/", views.ListStudent.as_view(), name="list-student"),
    path("delete-student/", views.DeleteStudent.as_view(), name="delete-student"),

    path("create-catelog/", views.NewCatelog.as_view(), name="create-catelog"),
    path("update-catelog/<int:pk>/", views.UpdateCatelog.as_view(), name="update-catelog"),
    path("list-catelog/", views.ListCatelog.as_view(), name="list-catelog"),
    path("delete-catelog/", views.DeleteCatelog.as_view(), name="delete-catelog"),

    path("provide-book/", views.ProvideBook.as_view(), name="provide-book"),
    path("list-provide/", views.ListProvide.as_view(), name="list-provide"),
    path("delete-provide/<int:pk>/", views.DeleteProvide.as_view(), name="delete-provide"),
    path("update-provide/<int:pk>/", views.UpdateProvide.as_view(), name="update-provide"),

    path("admin-login", views.ListAdmin.as_view(), name="admin-login"),

]
