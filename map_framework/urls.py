from django.urls import path
from map_app.views import home, despesa, orgao, instituicao, localizacao

urlpatterns = [
    path('', home.HomeView.as_view(), name = 'home'),
  
    path('gasto/list', despesa.DespesaListView.as_view(), name = 'despesa_list'),
    path('gasto/<int:pk>', despesa.DespesaDetailView.as_view(), name = 'despesa_detail'),
    path('gasto/cadastrar', despesa.DespesaCreateView.as_view(), name = 'despesa_create'),
    path('gasto/<int:pk>/update', despesa.DespesaUpdateView.as_view(), name = 'despesa_update'),
    
    path('local/list', orgao.OrgaoListView.as_view(), name = 'orgao_list'),
    path('local/<int:pk>', orgao.OrgaoDetailView.as_view(), name = 'orgao_detail'),
    path('local/cadastrar', orgao.OrgaoCreateView.as_view(), name = 'orgao_create'),
    path('local/<int:pk>/update', orgao.OrgaoUpdateView.as_view(), name = 'orgao_update'),

    path('localizacao/cadastrar', localizacao.LocalizacaoCreateView.as_view(), name = 'localizacao_create'),
    path('localizacao/<int:pk>/update', localizacao.LocalizacaoCreateView.as_view(), name = 'localizacao_update'),
]
