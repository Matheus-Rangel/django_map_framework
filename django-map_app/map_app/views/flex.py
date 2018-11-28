from django.views import View
from django.views.generic import TemplateView
from django.shortcuts import redirect
from map_app.models import Instituicao, Despesa, Orgao

class AtualizaView(View):

    def get(self, request):
        response = redirect('home')
        self.procedimento()
        return response

    def procedimento(self):
        pass

class ReclamaView(TemplateView):
    template_name = 'reclama.html'
    def get_context_data(self, **kwargs):
        context['despesa'] = Despesa.objects.filter(id = kwargs['pk'])

class InfoView(TemplateView):
    template_name = 'info.html'
    def get_context_data(self, **kwargs):
        context['instituicao'] = Instituicao.objects.all()
        context['orgao'] = Instituicao.objects.all()
        context['despesa'] = Despesa.objects.all()
        return context