from django.contrib import admin
from loan.models import Loan


class LoanAdmin(admin.ModelAdmin):
    list_display = ('summa', 'base')

admin.site.register(Loan, LoanAdmin)
