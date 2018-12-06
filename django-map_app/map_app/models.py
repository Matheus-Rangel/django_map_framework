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
        string = self.estado + ', ' + self.cidade +', ' + self.bairro
        if self.endereco != '':
            string += ', ' + self.endereco
        return string


class Instituicao(models.Model):
    class Meta:
        verbose_name = 'Instituição'
        verbose_name_plural = 'Instituições'
    nome = models.CharField(max_length = 256)
    telefone = models.CharField(max_length = 32, blank = True)
    email = models.EmailField(blank = True)
    site = models.URLField(blank = True)
    localizacao = models.ForeignKey(Localizacao, on_delete = models.SET_NULL, null = True)
    orgaos = models.ManyToManyField(
        'Orgao',
        through='OrgaoInstituicao',
    )
    def __str__(self):
        return self.nome

class Orgao(models.Model):
    class Meta:
        verbose_name = 'Orgão'
        verbose_name_plural = 'Orgãos'
    nome = models.CharField(max_length = 256)
    telefone = models.CharField(max_length = 32, blank = True)
    email = models.EmailField(blank = True)
    site = models.URLField(blank = True)
    localizacao = models.ForeignKey(Localizacao, on_delete = models.SET_NULL, null = True)
    instituicoes = models.ManyToManyField(
        'Instituicao',
        through='OrgaoInstituicao',
    )
    def __str__(self):
        return self.nome

class OrgaoInstituicao(models.Model):
    class Meta:
        verbose_name = 'Orgão e Instituicão'
        verbose_name_plural = 'Orgãos e Instituições'
    orgao = models.ForeignKey(Orgao, on_delete = models.CASCADE)
    instituicao = models.ForeignKey(Instituicao, on_delete = models.CASCADE)
    def __str__(self):
        return str(self.orgao) + ' - ' + str(self.instituicao)  

class Despesa(models.Model):
    descricao = models.TextField()
    elemento = models.TextField(blank=True)
    numero = models.CharField(max_length = 16)
    empenhado = models.DecimalField(max_digits=15, decimal_places=2)
    anulado = models.DecimalField(max_digits=15, decimal_places=2)
    liquidado = models.DecimalField(max_digits=15, decimal_places=2)
    pago = models.DecimalField(max_digits=15, decimal_places=2)

    data_inicio = models.DateField()
    data_update = models.DateField(auto_now = True)

    localizacao = models.ForeignKey(Localizacao, on_delete = models.SET_NULL, null = True, blank = True)

    # Orgao resonsavel pela obra
    orgao_instituicao = models.ForeignKey(OrgaoInstituicao, on_delete = models.CASCADE)
    def __str__(self):
        return self.descricao
