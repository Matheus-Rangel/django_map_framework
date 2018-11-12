from rest_framework import serializers
from map_app.models import Gasto, Local, Localizacao

class LocalizacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Localizacao
        fields = '__all__'

class LocalSerializer(serializers.ModelSerializer):
    localizacao = LocalizacaoSerializer(read_only=True)
    class Meta:
        model = Local
        fields = '__all__'

class GastoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gasto
        fields = 'all'
