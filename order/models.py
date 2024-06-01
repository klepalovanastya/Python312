from django.db import models

# Create your models here.

class Order(models.Model): #Раздел
    code = models.AutoField(primary_key=True, unique=True)
    buyerCode = models.IntegerField()
    orderDate = models.DateField(auto_now_add=True)
    deliveryDate = models.DateField()
    formOfPayment = models.CharField(max_length=120)
    typeOfDelivery = models.CharField(max_length=80)
    priceOfDelivery = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    address = models.CharField(max_length=500)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return self.code