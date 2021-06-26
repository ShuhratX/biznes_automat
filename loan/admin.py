from django.contrib import admin
from loan.models import Loan


class LoanAdmin(admin.ModelAdmin):
    list_display = ('summa', 'base', 'created_at')

admin.site.register(Loan, LoanAdmin)
