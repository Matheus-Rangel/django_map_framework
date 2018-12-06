from django.views import View
from django.views.generic import TemplateView
from django.shortcuts import redirect
from map_app.models import Instituicao, Despesa, Orgao, OrgaoInstituicao
from re import sub

class AtualizaView(TemplateView):
    template_name = 'map_app/atualiza.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        despesas = self.carregar_despesas()
        if type(despesas) != type(list()):
            AtualizaView.template_name = 'map_app/under_construction.html'
            return context        
        despesas_num = self.create_despesas(despesas)
        context["num_despesas_cadastradas"] = despesas_num[0]
        context["num_despesas"] = despesas_num[1]
        return context
    
    def carregar_despesas(self):
        pass

    def create_orgao_instituicao(self, orgao, instituicao):
        orgao_instituicao = OrgaoInstituicao(orgao=orgao, instituicao=instituicao)
        orgao_instituicao.save()
        return orgao_instituicao

    def create_orgao(self, nome_orgao):
        orgao = Orgao(nome=nome_orgao)
        orgao.save()
        return orgao

    def create_instituicao(self, nome_instituicao):
        instituicao = Instituicao(nome=nome_instituicao)
        instituicao.save()
        return instituicao

    def validar_instituicao(self, nome_instituicao):
        try: 
            instituicao = Instituicao.objects.get(nome = nome_instituicao)
        except Instituicao.DoesNotExist:
            instituicao = self.create_instituicao(nome_instituicao)
        return instituicao

    def validar_orgao(self, nome_orgao):
        try:
            orgao = Orgao.objects.get(nome=nome_orgao)
        except Orgao.DoesNotExist:
            orgao = self.create_orgao(nome_orgao)
        return orgao

    def validar_orgao_instituicao(self, orgao, instituicao):
        try:
            orgao_instituicao = OrgaoInstituicao.objects.get(orgao=orgao, instituicao=instituicao)
        except OrgaoInstituicao.DoesNotExist:
            orgao_instituicao = self.create_orgao_instituicao(orgao, instituicao)
        return orgao_instituicao

    def create_despesas(self, despesas):
        num_despesas_cadastradas = 0
        num_despesas = 0
        for despesa in despesas:
            num_despesas += 1
            try:
                instituicao = self.validar_instituicao(despesa['instituicao'])
                orgao = self.validar_orgao(despesa['orgao'])
                orgao_instituicao = self.validar_orgao_instituicao(orgao, instituicao)
                #Remove os pontos e virgulas dos valores caso venham
                empenhado = sub(r'[^\d,]', '', despesa['empenhado']).replace(',','.')
                anulado = sub(r'[^\d,]', '', despesa['anulado']).replace(',','.')
                liquidado = sub(r'[^\d,]', '', despesa['liquidado']).replace(',','.')
                pago = sub(r'[^\d,]', '', despesa['pago']).replace(',','.')
                descricao = despesa['descricao']
                data_inicio = despesa['data_inicio']
                elemento = despesa['elemento']
                numero = despesa['numero']
                try:
                    d = Despesa.objects.get(numero=numero, orgao_instituicao=orgao_instituicao)
                    d.descricao = descricao
                    d.elemento = elemento 
                    d.empenhado = empenhado
                    d.anulado = anulado 
                    d.liquidado = liquidado 
                    d.pago = pago 
                    d.data_inicio = data_inicio
                    d.save()
                except Despesa.DoesNotExist:
                    d = Despesa(descricao=descricao, elemento=elemento, numero=numero,
                                empenhado=empenhado, anulado=anulado, liquidado=liquidado,
                                pago=pago, data_inicio=data_inicio, orgao_instituicao=orgao_instituicao)
                    d.save()
                num_despesas_cadastradas += 1
            except KeyError as e:
                print("Despesa numero {} com formatação incorreta".format(num_despesas))
                continue
        return (num_despesas_cadastradas, num_despesas)

class ReclamaView(TemplateView):
    template_name = 'map_app/reclama.html'
    def get_context_data(self, **kwargs):
        pass

class InfoView(TemplateView):
    template_name = 'map_app/info.html'

    def get_context_data(self, **kwargs):
        context = super(InfoView, self).get_context_data(**kwargs)
        context['despesas_instituicoes'] = self.getInfoInstituicao()
        context['despesas_orgaos'] = self.getInfoOrgao()
        context['despesas_obras'] = self.getInfoDespesaObras()
        context['despesas_funcoes'] = self.getInfoDespesaFuncoes()
        return context

    def getInfoInstituicao(self):
        return ""

    def getInfoOrgao(self):
        return ""

    def getInfoDespesaObras(self):
        return ""

    def getInfoDespesaFuncoes(self):
        return ""

