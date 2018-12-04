from django.urls import path, include, re_path
from map_app.views import home, despesa, orgao, instituicao, localizacao, flex

from django_filters.views import FilterView
from map_app.filters import DespesaFilter, OrgaoFilter, InstituicaoFilter


urlpatterns = [
    path('', home.HomeView.as_view(), name = 'home'),

    re_path(r'^despesa/list/$', FilterView.as_view(filterset_class=DespesaFilter,
        template_name='map_app/despesa_list.html'), name='despesa_list'),
    path('despesa/<int:pk>', despesa.DespesaDetailView.as_view(), name = 'despesa_detail'),
    path('despesa/cadastrar', despesa.DespesaCreateView.as_view(), name = 'despesa_create'),
    path('despesa/<int:pk>/update', despesa.DespesaUpdateView.as_view(), name = 'despesa_update'),
    
    re_path(r'^orgao/list/$', FilterView.as_view(filterset_class=OrgaoFilter,
        template_name='map_app/orgao_list.html'), name='orgao_list'),
    path('orgao/<int:pk>', orgao.OrgaoDetailView.as_view(), name = 'orgao_detail'),
    path('orgao/cadastrar', orgao.OrgaoCreateView.as_view(), name = 'orgao_create'),
    path('orgao/<int:pk>/update', orgao.OrgaoUpdateView.as_view(), name = 'orgao_update'),
    
    re_path(r'^instituicao/list/$', FilterView.as_view(filterset_class=InstituicaoFilter,
        template_name='map_app/instituicao_list.html'), name='instituicao_list'),
    path('instituicao/<int:pk>', instituicao.InstituicaoDetailView.as_view(), name = 'instituicao_detail'),
    path('instituicao/cadastrar', instituicao.InstituicaoCreateView.as_view(), name = 'instituicao_create'),
    path('instituicao/<int:pk>/update', instituicao.InstituicaoUpdateView.as_view(), name = 'instituicao_update'),

    path('localizacao/cadastrar', localizacao.LocalizacaoCreateView.as_view(), name = 'localizacao_create'),
    path('localizacao/<int:pk>/update', localizacao.LocalizacaoUpdateView.as_view(), name = 'localizacao_update'),

    path('api/', include('map_app.api.urls.router')),

    path('reclamar/', include('reclama_app.urls')),
    path('atualizar/', include('atualiza_app.urls')),
    path('info/', include('info_app.urls')),
]