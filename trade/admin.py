from django.contrib import admin
from trade.models import Sale


class SaleAdmin(admin.ModelAdmin):
    list_display = ('summa', 'count')


admin.site.register(Sale, SaleAdmin)
