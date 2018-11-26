from django.contrib import admin
from map_app.models import Instituicao, Despesa, Orgao, Localizacao, OrgaoInstituicao
from rangefilter.filter import DateRangeFilter, DateTimeRangeFilter
# Register your models here.

admin.site.register(Despesa)
admin.site.register(Orgao)
admin.site.register(Instituicao)
admin.site.register(Localizacao)
admin.site.register(OrgaoInstituicao)
