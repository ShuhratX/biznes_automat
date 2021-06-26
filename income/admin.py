from django.contrib import admin
from .models import Income


class IncomeAdmin(admin.ModelAdmin):
    list_display = ('summa', 'partner', 'base', 'created_at')


admin.site.register(Income, IncomeAdmin)