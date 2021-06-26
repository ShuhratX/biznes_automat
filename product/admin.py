from django.contrib import admin

from .models import *


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'count')


class PartnerAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone')


class SaleAdmin(admin.ModelAdmin):
    list_display = ('summa', 'count')


class WorkerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'salary')


class LoanAdmin(admin.ModelAdmin):
    list_display = ('summa', 'base')


class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('summa', 'base')


admin.site.register(Product, ProductAdmin)
admin.site.register(Partner, PartnerAdmin)
admin.site.register(Sale, SaleAdmin)
admin.site.register(Worker, WorkerAdmin)
admin.site.register(Loan, LoanAdmin)
admin.site.register(Expense, ExpenseAdmin)