from django.contrib import admin
from django.urls import path
from map_app.api.views import orgao_instituicao
urlpatterns = [
    path('pk/<int:pk>', orgao_instituicao.OrgaoInstituicaoRetriveAPIView.as_view(), name = 'orgao_instituicao_id_retrive'),
    path('create', orgao_instituicao.OrgaoInstituicaoCreateAPIView.as_view(), name = 'orgao_instituicao_create'),
]