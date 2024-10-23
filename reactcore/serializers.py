from rest_framework import serializers
from .models import Books, Students, Catelog, Admin

class BooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = '__all__'

class StudentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = '__all__'

class CatelogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Catelog
        fields = '__all__'

class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = '__all__'