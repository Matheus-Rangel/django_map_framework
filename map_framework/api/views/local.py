from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from map_framework.models import Local
from map_framework.api.serializers import LocalSerializer

class LocalListAPIView(ListAPIView):
    serializer_class = LocalSerializer
    def get_queryset(self):
        return Local.objects.all()

class LocalRetriveAPIView(RetrieveAPIView):
    lookup_field = 'pk'
    serializer_class = LocalSerializer
    def get_queryset(self):
        return Local.objects.filter(id = self.kwargs['pk'])

class LocalNomeRetriveAPIView(RetrieveAPIView):
    lookup_field = 'nome'
    serializer_class = LocalSerializer
    def get_queryset(self):
        return Local.objects.filter(nome = self.kwargs['nome'])

class LocalCreateAPIView(CreateAPIView):
    serializer_class = LocalSerializer
    def get_queryset(self):
        return Local.objects.all()


