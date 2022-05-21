from django.db import models

# Create your models here.
class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    senha = models.CharField(max_length=40)
    data_nascimento = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.nome
