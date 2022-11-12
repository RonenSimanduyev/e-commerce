from email.policy import default
from itertools import product
from pyexpat import model
from venv import create
from django.db import models
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)
    imageUrl = models.CharField(max_length=1000)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    imageUrl = models.CharField(max_length=1000)

    def __str__(self):
        return self.name


class Order(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=12)
    time = models.DateTimeField(auto_now_add=True)
    product = models.ManyToManyField(Product)
