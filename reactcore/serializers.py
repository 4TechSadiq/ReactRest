from rest_framework import serializers
from .models import Books, Students, Catalog, Admin, Provide

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
        model = Catalog
        fields = '__all__'

class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = '__all__'

class ProvideSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provide
        fields = '__all__'