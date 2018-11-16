from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from map_app.models import  OrgaoInstituicao
from map_app.api.serializers import OrgaoInstituicaoSerializer

class OrgaoInstituicaoRetriveAPIView(RetrieveAPIView):
    lookup_field = 'pk'
    serializer_class = OrgaoInstituicaoSerializer
    def get_queryset(self):
        return OrgaoInstituicao.objects.filter(id = self.kwargs['pk'])

class OrgaoInstituicaoCreateAPIView(CreateAPIView):
    serializer_class = OrgaoInstituicaoSerializer
    def get_queryset(self):
        return Orgao.objects.all()
