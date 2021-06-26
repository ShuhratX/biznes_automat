from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer


class ProductCreateView(generics.CreateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()







