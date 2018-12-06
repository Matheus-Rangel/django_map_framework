from django.urls import path
from info_app.views import InfoNatalView

urlpatterns = [
    path('dados_gerais', InfoNatalView.as_view(), name='dados_gerais'),
]