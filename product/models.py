from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name = "Nomi")
    cost = models.PositiveIntegerField(verbose_name = "Tannarxi")
    price = models.PositiveIntegerField(verbose_name = "Narxi")
    count = models.PositiveIntegerField(verbose_name = "Soni")
    description = models.TextField(verbose_name = "Tafsilot")
    unit = models.CharField(max_length=15, verbose_name = "Birlik")


class Raw(models.Model):
    name = models.CharField(max_length=100, verbose_name = "Nomi")
    price = models.PositiveIntegerField(verbose_name = "Narxi")
    count = models.PositiveIntegerField(verbose_name = "Soni")
    unit = models.CharField(max_length=15, verbose_name = "Birlik")
    