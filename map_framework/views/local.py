from map_framework.models import Local
from map_framework.forms import LocalForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, ListView, CreateView, UpdateView

class LocalListView(ListView):
    model = Local
    def get_queryset(self):
        return Local.objects.all()

class LocalDetailView(DetailView):
    model = Local

class LocalCreateView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    form_class = LocalForm
    model = Local
    queryset = Local.objects.all()

class LocalUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    form_class = LocalForm
    model = Local
    queryset = Local.objects.all()