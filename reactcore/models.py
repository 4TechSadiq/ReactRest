from django.db import models

# Create your models here.
class Books(models.Model):
    book_name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    price = models.FloatField()
    publication = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.book_name
    
class Students(models.Model):
    student_name = models.CharField(max_length=100)
    user_ID = models.CharField(max_length=100)
    institution = models.CharField(max_length=100)
    book_chosen = models.ForeignKey(Books, on_delete=models.CASCADE)

    def __str__(self):
        return self.student
    
