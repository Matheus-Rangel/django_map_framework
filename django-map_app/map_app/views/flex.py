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
    template_name = 'map_app/info.html'

    def get_context_data(self, **kwargs):
        context = super(InfoView, self).get_context_data(**kwargs)

        context['despesas_instituicoes'] = self.getInfoInstituicao()
        context['despesas_orgaos'] = self.getInfoOrgao()
        context['despesas_obras'] = self.getInfoDespesaObras()
        return context

    def getInfoInstituicao(self):
        pass

    def getInfoOrgao(self):
        pass

    def getInfoDespesaObras(self):
        pass