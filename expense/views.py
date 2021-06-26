from rest_framework import generics
from expense.models import Expense
from expense.serializers import ExpenseSerializer


class ExpenseCreateView(generics.CreateAPIView):
    serializer_class = ExpenseSerializer
    queryset = Expense.objects.all()