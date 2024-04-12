from django.db import models
from django.db.models import DecimalField


# Create your models here.
class Books(models.Model):
    title = models.CharField(max_length=70)
    author = models.CharField(max_length=120)
    genre = models.CharField(max_length=40)
    year_of_publication = models.IntegerField()
    price = models.DecimalField(decimal_places=2, max_digits=5)
    number_of_copies = models.IntegerField()



