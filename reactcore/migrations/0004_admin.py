# Generated by Django 5.1.2 on 2024-10-23 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reactcore', '0003_remove_catelog_catelog_books_catelog_catelog_books'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adminID', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
    ]