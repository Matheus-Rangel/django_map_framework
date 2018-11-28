from django.urls import path
from map_app.views.flex import AtualizaView
from map_app.models import Despesa, Orgao, Instituicao, OrgaoInstituicao
import json
import os
from re import sub
from decimal import Decimal        
ROOTDIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'despesas')
INSTITUICOESDIR = [os.path.join(ROOTDIR, instituicao) for instituicao in os.listdir(ROOTDIR)]

class AtualizaNatalView(AtualizaView):
    def procedimento(self):
        for i in INSTITUICOESDIR:
            instituicao = self.validar_instituicao(os.path.basename(i))
            self.carregar_despesas(i, instituicao)

    def create_orgao_instituicao(self, orgao, instituicao):
        orgao_instituicao = OrgaoInstituicao(orgao=orgao, instituicao=instituicao)
        orgao_instituicao.save()
        return orgao_instituicao
        
    def create_orgao(self, nome_orgao, instituicao):
        orgao = Orgao(nome = nome_orgao)
        orgao.save()

    def create_instituicao(self, nome_instituicao):
        instituicao = Instituicao(nome=nome_instituicao)
        instituicao.save()
        return instituicao

    def validar_instituicao(self, nome_instituicao):
        instituicao = Instituicao.objects.filter(nome = nome_instituicao)
        if not instituicao:
            self.create_instituicao(nome_instituicao)
            instituicao = Instituicao.objects.filter(nome = nome_instituicao)
        return instituicao

    def validar_orgao(self, nome_orgao, instituicao):
        orgao = Orgao.objects.filter(nome = nome_orgao)
        if not orgao:
            self.create_orgao(nome_orgao, instituicao[0])
            orgao = Orgao.objects.filter(nome = nome_orgao)
        orgao_instituicao = OrgaoInstituicao.objects.filter(orgao=orgao[0], instituicao=instituicao[0])
        if not orgao_instituicao:
            self.create_orgao_instituicao(orgao[0], instituicao[0])
            orgao_instituicao = OrgaoInstituicao.objects.filter(orgao=orgao[0], instituicao=instituicao[0])
        return orgao_instituicao

    def create_despesas(self, despesas, orgao_instituicao):
        despesa_f = {}
        
        for despesa in despesas:
            despesa_f['empenhado'] = sub(r'[^\d,]', '', despesa['empenhado']).replace(',','.')
            despesa_f['anulado'] = sub(r'[^\d,]', '', despesa['anulado']).replace(',','.')
            despesa_f['liquidado'] = sub(r'[^\d,]', '', despesa['liquidado']).replace(',','.')
            despesa_f['pago'] = sub(r'[^\d,]', '', despesa['pago']).replace(',','.')
            despesa_f['descricao'] = despesa['historico']
            try:
                if despesa['itens'][0]['descricao'] == "NÃO UTILIZAR":
                    continue
            except:
                continue
            despesa_f['descricao'] += ". Itens: "
            for item in despesa['itens']:
                despesa_f['descricao'] += item['descricao'] + ". Quantidade: " + item['quantidade'] + ". Valor unitario: R$" + item['valor_unitario'] + ". Valor total: R$" + item['valor_total'] + "."
                dia, mes, ano = despesa['data'].split('/')
                despesa_f['data_inicio'] = ano + '-' + mes + '-' + dia
                despesa_f['elemento'] = despesa['elemento']
                despesa_f['numero'] = despesa['numero']
        
            try:
                d = Despesa.objects.get(numero=despesa_f['numero'], orgao_instituicao=orgao_instituicao[0])
                d.descricao = despesa_f['descricao']
                d.elemento = despesa_f['elemento'] 
                d.numero = despesa_f['numero'] 
                d.empenhado = despesa_f['empenhado']
                d.anulado = despesa_f['anulado'] 
                d.liquidado = despesa_f['liquidado'] 
                d.pago = despesa_f['pago'] 
                d.data_inicio = despesa_f['data_inicio']
                d.orgao_instituicao = orgao_instituicao[0]
                d.save()
            except Despesa.DoesNotExist:
                d = Despesa(descricao=despesa_f['descricao'], elemento=despesa_f['elemento'],
                            numero=despesa_f['numero'], empenhado=despesa_f['empenhado'],
                            anulado=despesa_f['anulado'], liquidado=despesa_f['liquidado'],
                            pago=despesa_f['pago'], data_inicio=despesa_f['data_inicio'],
                            orgao_instituicao=orgao_instituicao[0])
                d.save()

    def carregar_despesas(self, i, instituicao):
        for file in os.listdir(i):
            nome_orgao, ext = os.path.splitext(file)
            orgao_instuicao = self.validar_orgao(nome_orgao, instituicao)
            f = open(os.path.join(i, file), "rb")
            despesas = json.load(f)
            self.create_despesas(despesas, orgao_instuicao)

