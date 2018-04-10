from django.db import models
from pontozero_app.modelos import *


class Trabalho(models.Model):
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    data_inicio = models.DateField()
    data_fim = models.DateField()
    remuneracao = models.FloatField(null=True)
    descricao = models.CharField(max_length=500)

