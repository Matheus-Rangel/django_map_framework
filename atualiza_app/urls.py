from django.urls import path
from atualiza_app.views import AtualizaView

urls = [
    path('', AtualizaView.as_view(), name='atualiza'),
]