from django.contrib import admin
from django.urls import path
from map_framework.api.views import local
urlpatterns = [
    path('', local.LocalListAPIView.as_view(), name = 'local_list'),
    path('pk/<int:pk>', local.LocalRetriveAPIView.as_view(), name = 'local_id_retrive'),
    path('nome/<nome>', local.LocalNomeRetriveAPIView.as_view(), name = 'local_nome_retrive'),
    path('create', local.LocalCreateAPIView.as_view(), name = 'local_create'),
]