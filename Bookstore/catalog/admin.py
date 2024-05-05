from django.contrib import admin
from catalog.models import Book, Author, Category, PublishingHouse, Genre

# Register your models here.
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Category)
admin.site.register(Genre)
admin.site.register(PublishingHouse)