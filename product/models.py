from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nomi")
    price = models.PositiveIntegerField(verbose_name="Narxi")
    count = models.PositiveIntegerField(verbose_name="Soni")
    description = models.TextField(verbose_name="Tafsilot")


class Partner(models.Model):
    name = models.CharField(max_length=100, verbose_name="Ismi")
    phone = models.CharField(max_length=50, verbose_name="Telefon raqami")


class Sale(models.Model):
    count = models.PositiveIntegerField(verbose_name="Soni")
    paid = models.BooleanField(default=False, verbose_name="To'langan")
    summa = models.PositiveIntegerField(verbose_name="Summa")
    partner = models.ForeignKey(Partner, verbose_name="Hamkor", on_delete=models.DO_NOTHING)
    product = models.ForeignKey(Product, verbose_name="Maxsulot", on_delete=models.DO_NOTHING)


class Worker(models.Model):
    first_name = models.CharField(max_length=40, verbose_name="Ismi")
    last_name = models.CharField(max_length=40, verbose_name="Familiyasi")
    salary = models.PositiveIntegerField(verbose_name="Maoshi")


class Loan(models.Model):
    base = models.CharField(max_length=255, verbose_name="Asos")
    summa = models.PositiveIntegerField(verbose_name="Summa")
    closed = models.BooleanField(default=False, verbose_name="Yopilgan")
    partner = models.ForeignKey(Partner, verbose_name="Hamkor", on_delete=models.CASCADE)


class Expense(models.Model):
    summa = models.PositiveIntegerField(verbose_name="Summa")
    base = models.CharField(max_length=255, verbose_name="Asos")
    partner = models.ForeignKey(Partner, verbose_name="Hamkor", on_delete=models.CASCADE)
    worker = models.ForeignKey(Worker, verbose_name="Ishchi", on_delete=models.CASCADE)

