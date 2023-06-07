from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Shop(models.Model):
    productName = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    size = models.CharField(max_length=100)
    quantity = models.IntegerField()
    price = models.FloatField()
    image =  models.ImageField(null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__ (self):
        return self.productName
    
# class Cart(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    # products = models.ManyToManyField(Shop)
    # total_price = models.DecimalField(max_digits=6, decimal_places=2)