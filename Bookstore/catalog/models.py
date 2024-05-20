from django.db import models

# Create your models here.


class Section(models.Model): #Раздел
    title = models.CharField(max_length=100)
    slug = models.CharField(max_length=100, default='/')

    class Meta:
        verbose_name = 'Раздел'
        verbose_name_plural = 'Разделы'

    def __str__(self):
        return self.title

class PublishingHouse(models.Model):
    name = models.CharField(max_length=100, unique=True)
    city = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Издательство'
        verbose_name_plural = 'Издательства'

    def __str__(self):
        return self.name

class Author(models.Model):
    full_name = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'

    def __str__(self):
        return self.full_name


class Category(models.Model):
    title = models.CharField(max_length=70, unique=True, default='category')
    slug = models.CharField(max_length=100)
    section = models.ForeignKey(Section, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title

class Book(models.Model):
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=1000)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publishing_house = models.ForeignKey(PublishingHouse, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=100.00)
    category = models.ManyToManyField(Category,  null=True, blank=True)
    number_of_copies = models.IntegerField(default=1)
    year_of_publication = models.IntegerField(default=2000)
    number_of_pages = models.IntegerField(null=True)
    image = models.ImageField(upload_to='books_images/', blank=True, null=True)
    type_of_cover = models.CharField(max_length=100, default="твердая")
    amount = models.IntegerField(default=1)

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'

    def __str__(self):
        return self.title



