from django.contrib import admin
from django.urls import path
from map_framework.api.views import localizacao
urlpatterns = [
    path('<int:pk>/', localizacao.LocalizacaoAPIView.as_view(), name = 'localizacao_api'),
    path('', localizacao.LocalizacaoListAPIView.as_view(), name = 'localizacao_list_api'),
]
