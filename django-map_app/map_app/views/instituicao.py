from map_app.models import Instituicao, Despesa
from map_app.forms import InstituicaoForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, CreateView, UpdateView
import datetime

class InstituicaoDetailView(DetailView):
    model = Instituicao
    def get_context_data(self, **kwargs):
        now = datetime.datetime.now()
        context = super().get_context_data(**kwargs)
        context['ano'] = now.year
        despesas = Despesa.objects.filter(orgao_instituicao__instituicao=self.kwargs['pk'], data_inicio__year=now.year)
        empenhado = 0
        gasto = 0
        for despesa in despesas:
            empenhado += despesa.empenhado
            gasto += despesa.pago
        context['gasto'] = gasto
        context['empenhado'] = empenhado 
        return context

class InstituicaoCreateView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    redirect_field_name = 'map_app/instituicao_detail.html'
    form_class = InstituicaoForm
    model = Instituicao

class InstituicaoUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    redirect_field_name = 'map_app/instituicao_detail.html'
    form_class = InstituicaoForm
    model = Instituicao