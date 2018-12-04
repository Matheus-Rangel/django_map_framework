from django.shortcuts import render
from map_app.views.flex import InfoView
from map_app.models import Instituicao, Orgao, Despesa
import datetime
# Create your views here.
class InfoNatalView(InfoView):
    def getInfoInstituicao(self, **kwargs):
        try:
            ano = kwargs['ano']
        except KeyError:
            kwargs['ano'] = datetime.datetime.now().year
        instituicoes = Instituicao.objects.all()
        context = []
        for i in instituicoes:
            dic = {}
            dic['Instituição'] = i.nome
            despesas = Despesa.objects.filter(orgao_instituicao__instituicao=i, data_inicio__year=kwargs['ano'])
            empenhado = 0
            anulado = 0
            liquidado = 0
            pago = 0
            for d in despesas:
                empenhado += d.empenhado
                anulado += d.anulado
                liquidado += d.liquidado
                pago += d.pago
            dic['Pago'] = pago
            dic['Empenhado'] = empenhado
            dic['Liquidado'] =  liquidado
            dic['Anulado'] =  anulado
            context.append(dic)
        return context

    def getInfoOrgao(self, **kwargs):
        try:
            ano = kwargs['ano']
        except KeyError:
            kwargs['ano'] = datetime.datetime.now().year
        orgaos = Orgao.objects.all()
        context = []
        for o in orgaos:
            dic = {}
            dic['Orgão'] = o.nome
            despesas = Despesa.objects.filter(orgao_instituicao__orgao=o, data_inicio__year=kwargs['ano'])
            empenhado = 0
            anulado = 0
            liquidado = 0
            pago = 0
            for d in despesas:
                empenhado += d.empenhado
                anulado += d.anulado
                liquidado += d.liquidado
                pago += d.pago
            dic['Pago'] = pago
            dic['Empenhado'] = empenhado
            dic['Liquidado'] =  liquidado
            dic['Anulado'] =  anulado
            context.append(dic)
        return context
    
    def getInfoDespesaObras(self, **kwargs):
        try:
            ano = kwargs['ano']
        except KeyError:
            kwargs['ano'] = datetime.datetime.now().year
        orgaos = Orgao.objects.all()
        context = []
        for o in orgaos:
            dic = {}
            dic['Orgão'] = o.nome
            despesas = Despesa.objects.filter(orgao_instituicao__orgao=o, data_inicio__year=kwargs['ano'], elemento__icontains='OBRA')
            empenhado = 0
            anulado = 0
            liquidado = 0
            pago = 0
            for d in despesas:
                empenhado += d.empenhado
                anulado += d.anulado
                liquidado += d.liquidado
                pago += d.pago
            dic['Pago'] = pago
            dic['Empenhado'] = empenhado
            dic['Liquidado'] =  liquidado
            dic['Anulado'] =  anulado
            context.append(dic)
        return context