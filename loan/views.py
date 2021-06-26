from rest_framework import generics
from loan.models import Loan
from loan.serializers import LoanSerializer


class LoanCreateView(generics.CreateAPIView):
    serializer_class = LoanSerializer
    queryset = Loan.objects.all()
