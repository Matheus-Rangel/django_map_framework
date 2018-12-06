from map_app.models import Despesa, Orgao, Instituicao, OrgaoInstituicao
import django_filters

class DespesaFilter(django_filters.FilterSet):
    elemento = django_filters.CharFilter(lookup_expr='icontains')
    data_inicio = django_filters.NumberFilter(lookup_expr='year', initial='2018')
    orgao_instituicao__orgao__nome = django_filters.CharFilter(lookup_expr='icontains')
    orgao_instituicao__instituicao__nome = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Despesa
        fields = ['elemento', 'data_inicio', 'orgao_instituicao']
    
class InstituicaoFilter(django_filters.FilterSet):
    nome = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Instituicao
        fields = ['nome']
        
class OrgaoFilter(django_filters.FilterSet):
    nome = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Orgao
        fields = ['nome']
        