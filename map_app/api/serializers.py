
from rest_framework import serializers
from map_app.models import Despesa, Orgao, Instituicao, Localizacao, OrgaoInstituicao

class LocalizacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Localizacao
        fields = '__all__'

class OrgaoSerializer(serializers.ModelSerializer):
    localizacao = LocalizacaoSerializer(read_only=True)

    class Meta:
        model = Orgao
        fields = '__all__'

class DespesaSerializer(serializers.ModelSerializer):
    localizacao = LocalizacaoSerializer(read_only=True)
    orgao = OrgaoSerializer(read_only=True)

    class Meta:
        model = Despesa
        exclude = ['data_update']

class InstituicaoSerializer(serializers.ModelSerializer):
    localizacao = LocalizacaoSerializer(read_only=True)

    class Meta:
        model = Instituicao
        fields = '__all__'

class OrgaoInstituicaoSerializer(serializers.ModelSerializer):
    instituicao = InstituicaoSerializer(read_only=True)
    orgao = OrgaoSerializer(read_only=True)
    class Meta:
        model = OrgaoInstituicao
        fields = '__all__'
