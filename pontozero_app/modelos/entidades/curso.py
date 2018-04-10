from django.db import models
from pontozero_app.modelos import *


class Curso(models.Model):
    nome = models.CharField(max_length=200)
    codigo = models.IntegerField(primary_key=True)
    instituicao = models.ForeignKey(Instituicao, on_delete=models.CASCADE)
    carga_horaria = models.IntegerField()
    data_inicio = models.DateField()
    data_fim = models.DateField()

