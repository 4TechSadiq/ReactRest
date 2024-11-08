from django.db import models

class Books(models.Model):
    book_name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    isbnumber = models.IntegerField()
    image = models.CharField(max_length=500)
    price = models.FloatField()
    publication = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.book_name

class Students(models.Model):
    student_name = models.CharField(max_length=100)
    user_ID = models.CharField(max_length=100, unique=True)
    institution = models.CharField(max_length=100)
    profile = models.CharField(max_length=500)

    def __str__(self):
        return self.user_ID

class Catalog(models.Model):
    catalog_name = models.CharField(max_length=500)
    catalog_desc = models.CharField(max_length=500)
    catalog_books = models.ManyToManyField(Books, related_name="catalogs")
    catalog_image = models.CharField(max_length=500)

    def __str__(self):
        return self.catalog_name

class Admin(models.Model):
    adminID = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.adminID

class Provide(models.Model):
    student = models.ForeignKey(Students, on_delete=models.CASCADE)
    book = models.CharField(max_length=300)
    approved_date = models.DateField(auto_now_add=True)
    return_date = models.DateField()

    def __str__(self):
        return f"{self.student.user_ID} - {self.book.book_name}"

