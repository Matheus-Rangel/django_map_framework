from django.urls import path
from info_app.views import InfoRecifeView

urlpatterns = [
    path('dados_gerais', InfoRecifeView.as_view(), name='dados_gerais'),
]