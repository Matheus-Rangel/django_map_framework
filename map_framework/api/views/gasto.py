from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from map_framework.models import Gasto
from map_framework.api.serializers import GastoSerializer

import datetime

class GastoCreateAPIView(CreateAPIView):
    serializer_class = GastoSerializer
    def get_queryset(self):
        return Gasto.objects.filter(pk = self.kwargs['pk'])

class GastoRetriveAPIView(RetrieveAPIView):
    serializer_class = GastoSerializer
    def get_queryset(self):
        return Gasto.objects.filter(pk = self.kwargs['pk'])
