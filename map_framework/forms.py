from django import forms
from map_framework.models import Gasto, Local, Instituicao, Localizacao, Comentario

class GastoForm(forms.ModelForm):
    class Meta():
        model = Gasto
        fields = '__all__'

class LocalForm(forms.ModelForm):
    class Meta():
        model = Local
        fields = '__all__'


class LocalizacaoForm(forms.ModelForm):
    class Meta():
        model = Localizacao
        fields = '__all__'
