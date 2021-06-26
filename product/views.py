from rest_framework import generics
from .models import *
from .serializers import *


class ProductCreateView(generics.CreateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class PartnerCreateView(generics.CreateAPIView):
    serializer_class = PartnerSerializer
    queryset = Partner.objects.all()


class SaleCreateView(generics.CreateAPIView):
    serializer_class = SaleSerializer
    queryset = Sale.objects.all()


class WorkerCreateView(generics.CreateAPIView):
    serializer_class = WorkerSerializer
    queryset = Worker.objects.all()


class LoanCreateView(generics.CreateAPIView):
    serializer_class = LoanSerializer
    queryset = Loan.objects.all()


class ExpenseCreateView(generics.CreateAPIView):
    serializer_class = ExpenseSerializer
    queryset = Expense.objects.all()
