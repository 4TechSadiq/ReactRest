# Generated by Django 5.1.2 on 2024-10-23 12:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
                ('price', models.FloatField()),
                ('publication', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Catelog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('catelog_name', models.CharField(max_length=500)),
                ('catelog_desc', models.CharField(max_length=500)),
                ('catelog_books', models.CharField(max_length=500)),
                ('catelog_image', models.ImageField(upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=100)),
                ('user_ID', models.CharField(max_length=100)),
                ('institution', models.CharField(max_length=100)),
                ('book_chosen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reactcore.books')),
            ],
        ),
    ]
