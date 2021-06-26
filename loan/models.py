from django.db import models

from partner.models import Partner


class Loan(models.Model):
    TYPE_CHOICES = (('debit', 'Debitor'), ('kredit', 'Kreditor'),)
    base = models.CharField(max_length=255, verbose_name="Asos")
    summa = models.PositiveIntegerField(verbose_name="Summa")
    closed = models.BooleanField(default=False, verbose_name="Yopilgan")
    partner = models.ForeignKey(Partner, verbose_name="Hamkor", on_delete=models.CASCADE)
    variation = models.CharField(max_length=15, choices=TYPE_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

