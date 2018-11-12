from django.db import models
from django.utils import timezone

class Localizacao(models.Model):
    class Meta:
        verbose_name = 'localização'
        verbose_name_plural = 'localizações'
    estado = models.CharField(max_length = 2)
    cidade = models.CharField(max_length = 50)
    bairro = models.CharField(max_length = 50)
    endereco = models.CharField(max_length = 256, blank = True)
    cep = models.CharField(max_length = 8, blank = True)

    latitude = models.DecimalField(null = False, max_digits=12, decimal_places=9)
    longitude = models.DecimalField(null = False, max_digits=12, decimal_places=9)
    def __str__(self):
        str = self.estado + ', ' + self.cidade +', ' + self.bairro
        if self.endereco != '':
            str += ', ' + self.endereco
        return str


class Local(models.Model):
    class Meta:
        verbose_name = 'Local'
        verbose_name_plural = 'Locais'
    nome = models.CharField(max_length = 256)
    localizacao = models.ForeignKey(Localizacao, on_delete = models.SET_NULL, null = True)
    def __str__(self):
        return self.nome

class Gasto(models.Model):
    class Meta:
        verbose_name = 'Gasto'
        verbose_name_plural = 'Gastos'
    descricao = models.TextField()
    valor = models.DecimalField(max_digits=15, decimal_places=2)
    def __str__(self):
        return self.descricao
