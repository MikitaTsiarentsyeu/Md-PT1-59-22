from django.db import models


class Catalog(models.Model):
    catalog_name = models.TextField(unique=True)


class Products(models.Model):
    SYSTEM_CURRENCY = [('USD', "USD"), ('RUB', "RUB")]

    name = models.CharField(max_length=100, unique=True)
    product_type = models.ForeignKey('Catalog', on_delete=models.CASCADE, max_length=100)
    description = models.TextField()
    currency = models.CharField(max_length=3, choices=SYSTEM_CURRENCY)
    price = models.IntegerField()


class Bascet(models.Model):
    SYSTEM_CURRENCY = [('USD', "USD"), ('RUB', "RUB")]

    user = models.CharField(max_length=100)
    name = models.ForeignKey('Products', max_length=100, blank=True, on_delete=models.CASCADE)
    description = models.TextField()
    currency = models.CharField(max_length=3, choices=SYSTEM_CURRENCY)
    price = models.IntegerField()
