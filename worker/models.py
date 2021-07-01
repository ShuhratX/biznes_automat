from django.db import models


class Worker(models.Model):
    first_name = models.CharField(max_length=40, verbose_name="Ismi")
    last_name = models.CharField(max_length=40, verbose_name="Familiyasi")
    phone = models.CharField(max_length=50, verbose_name="Telefon raqami")
    salary = models.PositiveIntegerField(verbose_name="Maoshi")

