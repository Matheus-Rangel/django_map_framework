from django.contrib import admin
from map_framework.models import Local, Gasto, Localizacao
from rangefilter.filter import DateRangeFilter, DateTimeRangeFilter
# Register your models here.

admin.site.register(Gasto)
admin.site.register(Local)
admin.site.register(Localizacao)
