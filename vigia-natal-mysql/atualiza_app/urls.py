from django.urls import path
from atualiza_app.views import AtualizaNatalView

urlpatterns = [
    path('', AtualizaNatalView.as_view(), name='atualiza'),
]