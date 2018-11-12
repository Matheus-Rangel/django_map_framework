from map_framework.models import Localizacao
from map_framework.forms import LocalizacaoForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, UpdateView

class LocalizacaoCreateView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    form_class = LocalizacaoForm
    model = Localizacao
    queryset = Localizacao.objects.all()

class LocalizacaoUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    form_class = LocalizacaoForm
    model = Localizacao
    queryset = Localizacao.objects.all()