from django.db import models
from partner.models import Partner
from worker.models import Worker


class Expense(models.Model):
    summa = models.PositiveIntegerField(verbose_name="Summa")
    base = models.CharField(max_length=255, verbose_name="Asos")
    partner = models.ForeignKey(Partner, verbose_name="Hamkor", null=True, on_delete=models.CASCADE)
    worker = models.ForeignKey(Worker, verbose_name="Ishchi", null=True, on_delete=models.CASCADE)
