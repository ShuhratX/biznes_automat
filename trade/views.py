from rest_framework import generics, status
from rest_framework.response import Response
from income.models import Income
from loan.models import Loan
from product.models import Product
from trade.models import Sale
from trade.serializers import SaleSerializer


class SaleCreateView(generics.GenericAPIView):
    serializer_class = SaleSerializer

    @staticmethod
    def post(request):
        count = int(request.data.get('count'))
        paid = str(request.data.get('paid')).capitalize()
        partner = request.data.get('partner')
        product = request.data.get('product')
        prod = Product.objects.get(id=product)
        summa = prod.price * count
        base = f"{prod.name} sotuvi"
        if paid == 'True':
            Income.objects.create(summa=summa, partner_id=partner, base=base)
        else:
            paid = False
            Loan.objects.create(variation = 'debit', base=base, summa=summa, partner_id=partner, closed=False)
        Sale.objects.create(count=count, paid=paid, partner_id=partner, product_id=product, summa=summa)
        return Response("Muvaffaqiyatli", status=status.HTTP_200_OK)