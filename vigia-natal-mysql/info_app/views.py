from django.shortcuts import render
from map_app.views.flex import InfoView
from info_app.models import OrgaoGastos, InstituicaoGastos, ElementoGastos
import datetime
# Create your views here.
class InfoNatalView(InfoView):
    def getInfoInstituicao(self, **kwargs):
        try:
            ano = kwargs['ano']
        except KeyError:
            kwargs['ano'] = datetime.datetime.now().year
        instituicoes = InstituicaoGastos.objects.all()
        context = []
        for i in instituicoes:
            dic = {}
            dic['Instituição'] = i.nome
            dic['Pago'] = i.pago
            dic['Empenhado'] = i.empenhado
            dic['Liquidado'] =  i.liquidado
            dic['Anulado'] =  i.anulado
            context.append(dic)
        return context

    def getInfoOrgao(self, **kwargs):
        try:
            ano = kwargs['ano']
        except KeyError:
            kwargs['ano'] = datetime.datetime.now().year
        orgaos = OrgaoGastos.objects.all()
        context = []
        for o in orgaos:
            dic = {}
            dic['Instituição'] = o.nome
            dic['Pago'] = o.pago
            dic['Empenhado'] = o.empenhado
            dic['Liquidado'] =  o.liquidado
            dic['Anulado'] =  o.anulado
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