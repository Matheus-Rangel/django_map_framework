from django.urls import path
from map_app.views.home import HomeView

urlpatterns = [
    path('', HomeView.as_view(), name='atualiza'),
]