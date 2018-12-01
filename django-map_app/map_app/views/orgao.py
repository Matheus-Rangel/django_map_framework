from map_app.models import Orgao, Despesa
from map_app.forms import OrgaoForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, CreateView, UpdateView

import datetime

class OrgaoDetailView(DetailView):
    model = Orgao
    def get_context_data(self, **kwargs):
        now = datetime.datetime.now()
        context = super().get_context_data(**kwargs)
        context['ano'] = now.year
        despesas = Despesa.objects.filter(orgao_instituicao__orgao=self.kwargs['pk'], data_inicio__year=now.year)
        empenhado = 0
        gasto = 0
        for despesa in despesas:
            empenhado += despesa.empenhado
            gasto += despesa.pago
        context['gasto'] = gasto
        context['empenhado'] = empenhado 
        return context

class OrgaoCreateView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    redirect_field_name = 'map_app/orgao_detail.html'
    form_class = OrgaoForm
    model = Orgao

class OrgaoUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    redirect_field_name = 'map_app/orgao_detail.html'
    form_class = OrgaoForm
    model = Orgao