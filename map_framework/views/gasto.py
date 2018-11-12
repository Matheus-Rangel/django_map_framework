from map_app.models import Gasto
from map_app.forms import GastoForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, ListView, CreateView, UpdateView

class GastoListView(ListView):
    model = Gasto
    def get_queryset(self):
        return Gasto.objects.all()

class GastoDetailView(DetailView):
    model = Gasto

class GastoCreateView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    form_class = GastoForm
    model = Gasto
    queryset = Gasto.objects.all()
 
class GastoUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    form_class = GastoForm
    model = Gasto
    queryset = Gasto.objects.all()