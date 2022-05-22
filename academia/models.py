from django.db import models
from django.utils.translation import ugettext as _
from usuarios.models import Usuario
from django.contrib.auth.models import User

MONDEY = 1
TUESDAY = 2
WEDNESDAY = 3
THURSDAY = 4
FRIDAY = 5
SATURDAY = 6
SUNDAY = 7

DIAS = [
	(MONDEY, _('Segunda-Feira')),
	(TUESDAY, _('Terça-Feira')),
	(WEDNESDAY, _('Quarta-Feira')),
	(THURSDAY, _('Quinta-Feira')),
	(FRIDAY, _('Sexta-Feira')),
	(SATURDAY, _('Sábado')),
	(SUNDAY, _('Domingo')),
]

class Exercicio(models.Model):
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.descricao

class TipoTreino(models.Model):
    descricao = models.CharField(max_length=100) #Treino A, B, C
    exercicio = models.ManyToManyField(Exercicio)
    def __str__(self):
        return self.descricao
    
class DiaSemana(models.Model):
    dia = models.IntegerField(choices=DIAS)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    treino = models.ManyToManyField(TipoTreino)

    def __str__(self):
        return "{0} - {1}".format(self.usuario.nome, self.get_dia_display())

