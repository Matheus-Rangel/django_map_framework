from django.urls import path
from info_app.views import InfoFortalezaView

urlpatterns = [
    path('dados_gerais', InfoFortalezaView.as_view(), name='dados_gerais'),
]