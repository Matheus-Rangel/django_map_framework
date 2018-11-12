from django.contrib import admin
from django.urls import path
from map_framework.api.views import gasto 
urlpatterns = [
    path('id/<int:pk>', gasto.GastoRetriveAPIView.as_view(), name='gasto_id_retrive'),
    path('create', gasto.GastoCreateAPIView.as_view(), name = 'gasto_create'),
]