from django.db import models

# Create your models here.

class Partner(models.Model):
    name = models.CharField(max_length=100, verbose_name="Ismi")
    phone = models.CharField(max_length=50, verbose_name="Telefon raqami")
