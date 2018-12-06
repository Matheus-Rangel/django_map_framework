import json
import os
import datetime
from map_app.models import Orgao, Despesa, Instituicao
from django.shortcuts import render
from django.contrib.humanize.templatetags.humanize import intcomma

# Create your views here.
from map_app.views.flex import InfoView

def formatterString( string ):
    float_num = round( float(string.replace('"', '')), 2)
    float_f = intcomma(float_num)
    return float_f

class InfoNatalView(InfoView):
    def getInfoInstituicao(self):
        now = datetime.datetime.now()
        list_inst = Instituicao.objects.all()
        list_desp = Despesa

        data = []

        for inst in list_inst:
            list_desp = Despesa.objects.filter(orgao_instituicao__instituicao=inst.pk, data_inicio__year=now.year)
            
            empenhado = 0
            pago = 0
            anulado = 0
            liquidado = 0

            for despesa in list_desp:
                empenhado += despesa.empenhado
                pago += despesa.pago
                anulado += despesa.anulado
                liquidado += despesa.liquidado

            dic = {}
            dic['Instituição'] = inst.nome
            dic['Empenhado'] = formatterString( str(empenhado) )
            print(dic['Empenhado'])
            dic['Pago'] = formatterString( str(pago) )
            dic['Liquidado'] = formatterString( str(liquidado) )
            dic['Anulado'] = formatterString( str(anulado) )

            data.append(dic)

        return data

    def getInfoOrgao(self):
        now = datetime.datetime.now()
        list_org = Orgao.objects.all()
        list_desp = Despesa

        data = []

        for org in list_org:
            list_desp = Despesa.objects.filter(orgao_instituicao__instituicao=org.pk, data_inicio__year=now.year)
            
            empenhado = 0
            pago = 0
            anulado = 0
            liquidado = 0

            for despesa in list_desp:
                empenhado += despesa.empenhado
                pago += despesa.pago
                anulado += despesa.anulado
                liquidado += despesa.liquidado

            dic = {}
            dic['Orgão'] = org.nome
            dic['Empenhado'] = formatterString( str(empenhado) )
            print(dic['Empenhado'])
            dic['Pago'] = formatterString( str(pago) )
            dic['Liquidado'] = formatterString( str(liquidado) )
            dic['Anulado'] = formatterString( str(anulado) )

            data.append(dic)

        return data