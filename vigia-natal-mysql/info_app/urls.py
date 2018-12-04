from django.urls import path
from info_app.views import InfoNatalView

urlpatterns = [
    path('<int:ano>', InfoNatalView.as_view(), name='dados_gerais_ano'),
    path('', InfoNatalView.as_view(), name='dados_gerais'),
]