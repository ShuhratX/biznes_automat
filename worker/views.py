from rest_framework import generics

from worker.models import Worker
from worker.serializers import WorkerSerializer


class WorkerCreateView(generics.CreateAPIView):
    serializer_class = WorkerSerializer
    queryset = Worker.objects.all()

