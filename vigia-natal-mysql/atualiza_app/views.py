from django.urls import path
from map_app.views.flex import AtualizaView
from map_app.models import Despesa, Orgao, Instituicao, OrgaoInstituicao
import json
import os
from re import sub

DESPESASDIRS = []
ROOTDIR = os.path.dirname(os.path.abspath(__file__))
ROOTDIR = os.path.join(ROOTDIR, 'Despesas')
INSTITUICOESDIR = []
for d in os.listdir(ROOTDIR):
    if d.startswith('Despesas'):
        DESPESASDIRS.append(os.path.join(ROOTDIR, d))
for DESPESADIR in DESPESASDIRS:
    for instituicao in os.listdir(DESPESADIR):
        INSTITUICOESDIR.append(os.path.join(DESPESADIR, instituicao))

class AtualizaNatalView(AtualizaView):
    def carregar_despesas(self):
        despesas = []
        for i in INSTITUICOESDIR:
            instituicao = os.path.basename(i)
            for file in os.listdir(i):
                orgao, ext = os.path.splitext(file)
                f = open(os.path.join(i, file), "rb")
                dados = json.load(f)
                for dado in dados:
                    despesa = {}
                    despesa['orgao'] = orgao
                    despesa['instituicao'] = instituicao
                    despesa['descricao'] = dado['historico']
                    despesa['elemento'] = dado['elemento']
                    despesa['numero'] = dado['numero']
                    despesa['empenhado'] = sub(r'[^\d,]', '', dado['empenhado']).replace(',','.')
                    despesa['anulado'] = sub(r'[^\d,]', '', dado['anulado']).replace(',','.')
                    despesa['liquidado'] = sub(r'[^\d,]', '', dado['liquidado']).replace(',','.')
                    despesa['pago'] = sub(r'[^\d,]', '', dado['pago']).replace(',','.')
                    
                    dia, mes, ano = dado['data'].split('/')
                    despesa['data_inicio'] = ano + '-' + mes + '-' + dia
                    despesas.append(despesa)
        return despesas