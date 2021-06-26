from rest_framework import generics

from partner.models import Partner
from partner.serializers import PartnerSerializer


class PartnerCreateView(generics.CreateAPIView):
    serializer_class = PartnerSerializer
    queryset = Partner.objects.all()
