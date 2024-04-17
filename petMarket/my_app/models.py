from django.db import models


# Create your models here.
class Books(models.Model):
    title = models.CharField(max_length=70)
    author = models.CharField(max_length=120, null=True)
    genre = models.CharField(max_length=40, null=True)
    year_of_publication = models.IntegerField(null=True)
    price = models.DecimalField(decimal_places=2, max_digits=5, default=100)
    number_of_copies = models.IntegerField(default=1)

class Tasks(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200, )
    status = models.CharField(max_length=30, null=True)
    date_created = models.DateField(auto_now_add=True)
