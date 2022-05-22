from django.contrib import admin

from academia.models import DiaSemana, Exercicio, TipoTreino

# Register your models here.
admin.site.register(DiaSemana)
admin.site.register(TipoTreino)
admin.site.register(Exercicio)