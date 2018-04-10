from django.db import models
from pontozero_app.modelos import *


class Vaga(models.Model):
    nome = models.CharField(max_length=200)
    data_abertura = models.DateField()
    setor = models.CharField(max_length=100)
    funcao = models.CharField(max_length=100)
    descricao = models.TextField()
    empresa_responsavel = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    estudantes = models.ManyToManyField(Estudante)
