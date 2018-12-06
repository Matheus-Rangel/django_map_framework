import json
import csv
import os
from django.shortcuts import render
from django.contrib.humanize.templatetags.humanize import intcomma

# Create your views here.
from map_app.views.flex import InfoView

def formatterString( string ):
    float_num = round( float(string.replace('"', '')), 2)
    float_f = intcomma(float_num)
    result = float_f.replace('.', ';').replace(',', '.').replace(';', ',')
    return result   

class InfoRecifeView(InfoView):
    def getInfoInstituicao(self):
        path = os.path.dirname(os.path.realpath(__file__))
        csv_data = []
        with open(path + '\static\csv\despesas_orgaos.csv', 'rt', encoding="utf8") as ficheiro:
            reader = csv.reader(ficheiro)
            next(reader)
            for linha in reader:
                itens = linha[0].split(',"')
                dic = {}
                dic['Instituição'] = itens[0]
                dic['Empenhado'] = formatterString(itens[1])
                dic['Pago'] = formatterString(itens[2])
                dic['Liquidado'] = formatterString(itens[3])
                dic['Anulado'] = "0,00"
                
                csv_data.append(dic)
        
        return csv_data

    def getInfoOrgao(self):
        path = os.path.dirname(os.path.realpath(__file__))
        csv_data = []
        with open(path + '\static\csv\despesas_unidades.csv', 'rt', encoding="utf8") as ficheiro:
            reader = csv.reader(ficheiro)
            next(reader)
            for linha in reader:
                itens = linha[0].split(',"')
                dic = {}
                dic['Orgão'] = itens[0]
                dic['Empenhado'] = formatterString(itens[1])
                dic['Pago'] = formatterString(itens[2])
                dic['Liquidado'] = formatterString(itens[3])
                dic['Anulado'] = "0,00"
                
                csv_data.append(dic)
            
        return csv_data