# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

from datetime import datetime

# Create your models here.
class Customer(models.Model): 
    customer_name = models.CharField(max_length=250)

    def __str__(self):
        return self.customer_name

class Machine(models.Model):
    weight = models.IntegerField()
    min_profit_per_hour = models.DecimalField(max_digits=10, decimal_places=5)


class Product(models.Model):
    product_code = models.CharField(max_length=250)
    product_description = models.TextField()
    customer = models.ManyToManyField(Customer)
    machine = models.ManyToManyField(Machine)

    def __str__(self):
        return self.product_code

class ProductPrice(models.Model):
    FLAG_CHOICES = (
        ('Y', 'Y'),
        ('N', 'N')
    )
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    min_order_quantity = models.IntegerField(null=False)
    start_date = models.DateTimeField(default=datetime.now(), null=True)
    end_date = models.DateTimeField(default=datetime(2999, 12, 31, 18, 00), null=True)
    current_flag = models.CharField(max_length=1, choices=FLAG_CHOICES)
    version = models.IntegerField()

    def __str__(self):
        return f"{self.product} ({self.min_order_quantity}) {self.current_flag}"