from django.db import models
from catalog.models import Book
# Create your models here.

class Feedback(models.Model):
    text = models.CharField(max_length=200)
    rating = models.IntegerField(default=1)
    image = models.ImageField(upload_to='feedback_images/', blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    book = models.ForeignKey(Book, default=1, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

