from django.contrib import admin
from django.urls import path, include
 
urlpatterns = [
    path('gasto/', include('map_app.api.urls.despesa')),
    path('local/', include('map_app.api.urls.instituicao')),
    path('localizacao/', include('map_app.api.urls.localizacao')),
]