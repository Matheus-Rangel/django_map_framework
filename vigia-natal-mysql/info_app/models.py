from django.db import models

class OrgaoGastos(models.Model):
    id = models.BigIntegerField(primary_key=True)
    nome = models.CharField(max_length = 256)
    empenhado = models.DecimalField(max_digits=15, decimal_places=2)
    anulado = models.DecimalField(max_digits=15, decimal_places=2)
    liquidado = models.DecimalField(max_digits=15, decimal_places=2)
    pago = models.DecimalField(max_digits=15, decimal_places=2)
    
    class Meta:
        managed = False
        db_table = 'map_app_orgaogastos'

class InstituicaoGastos(models.Model):
    id = models.BigIntegerField(primary_key=True)
    nome = models.CharField(max_length = 256)
    empenhado = models.DecimalField(max_digits=15, decimal_places=2)
    anulado = models.DecimalField(max_digits=15, decimal_places=2)
    liquidado = models.DecimalField(max_digits=15, decimal_places=2)
    pago = models.DecimalField(max_digits=15, decimal_places=2)
    
    class Meta:
        managed = False
        db_table = 'map_app_instituicaogastos'

class ElementoGastos(models.Model):
    elemento = models.TextField(blank=True)
    empenhado = models.DecimalField(max_digits=15, decimal_places=2)
    anulado = models.DecimalField(max_digits=15, decimal_places=2)
    liquidado = models.DecimalField(max_digits=15, decimal_places=2)
    pago = models.DecimalField(max_digits=15, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'map_app_elementogastos'