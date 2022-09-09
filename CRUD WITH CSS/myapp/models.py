from django.db import models
#from django.utils import timezone
# Create your models here.


class Products(models.Model):
    title = models.CharField(max_length=200)
    price = models.IntegerField()
    category =  models.CharField(max_length =100)
    description = models.TextField()
    image =  models.ImageField(blank=True,)

    def __str__(self):
        return self.title










































































#https://fakestoreapi.com/products
#'https://fakestoreapi.com/products/1