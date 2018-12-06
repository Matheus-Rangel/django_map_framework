import json
import os
from django.shortcuts import render

# Create your views here.
from map_app.views.flex import InfoView

class InfoFortalezaView(InfoView):
    def getInfoOrgao(self):
        path = os.path.dirname(os.path.realpath(__file__))
        with open(path + '\static\json\despesas_orgaos.json', encoding="utf8") as json_file:
            json_data = json.load(json_file)
        return json_data

    def getInfoDespesaFuncoes(self):
        path = os.path.dirname(os.path.realpath(__file__))
        with open(path + '\static\json\despesas_funcoes.json', encoding="utf8") as json_file:
            json_data = json.load(json_file)
        return json_data