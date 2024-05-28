from django.contrib import admin

from order.models import Order


# Register your models here.
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('code', 'buyerCode', 'orderDate')
    list_display_links = ('code', )