from django.urls import path
from map_app.views.flex import AtualizaView

urls = [
    path('', AtualizaNatalView.as_view(), name='atualiza'),
]