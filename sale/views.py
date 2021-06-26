from rest_framework import generics

from sale.models import Sale
from sale.serializers import SaleSerializer


class SaleCreateView(generics.CreateAPIView):
    serializer_class = SaleSerializer
    queryset = Sale.objects.all()
