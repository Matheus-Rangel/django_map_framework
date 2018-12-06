import json
from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = 'map_app/home.html'