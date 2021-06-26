from django.db import models
from partner.models import Partner
from product.models import Product


class Sale(models.Model):
    count = models.PositiveIntegerField(verbose_name="Soni")
    paid = models.BooleanField(default=False, verbose_name="To'langan")
    summa = models.PositiveIntegerField(verbose_name="Summa")
    partner = models.ForeignKey(Partner, verbose_name="Hamkor", on_delete=models.DO_NOTHING)
    product = models.ForeignKey(Product, verbose_name="Maxsulot", on_delete=models.DO_NOTHING)

