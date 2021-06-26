from django.db import models

from partner.models import Partner


class Income(models.Model):
    summa = models.PositiveIntegerField(verbose_name="Summa")
    partner = models.ForeignKey(Partner, verbose_name="Hamkor", on_delete=models.DO_NOTHING)
    base = models.CharField(max_length=255, verbose_name="Asos")