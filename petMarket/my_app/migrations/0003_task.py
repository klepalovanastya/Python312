# Generated by Django 4.2.1 on 2024-04-13 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0002_alter_books_author_alter_books_genre_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=120, null=True)),
                ('status', models.CharField(max_length=30)),
                ('date_created', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
