from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural= 'Категории'

class PublishingHouse(models.Model):
    name = models.CharField(max_length=100, unique=True)
    city = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Издательство'
        verbose_name_plural= 'Издательства'

class Author(models.Model):
    full_name = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural= 'Авторы'


class Genre(models.Model):
    name = models.CharField(max_length=70, unique=True)

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural= 'Жанры'

class Book(models.Model):
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=1000)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publishing_house = models.ForeignKey(PublishingHouse, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=100.00)
    category = models.ManyToManyField(Category,  null=True, blank=True)
    genre = models.ManyToManyField(Genre, null=True, blank=True)
    number_of_copies = models.IntegerField(default=1)
    year_of_publication = models.IntegerField(default=2000)
    number_of_pages = models.IntegerField(null=True)
    image = models.ImageField(upload_to='books_images/', blank=True, null=True)

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural= 'Книги'



