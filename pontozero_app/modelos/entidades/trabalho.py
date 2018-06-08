from django.db import models
from pontozero_app.modelos.entidades.pessoa import Pessoa
from pontozero_app.modelos.entidades.empresa import Empresa


class Trabalho(models.Model):
    identificador = models.IntegerField(primary_key=True)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    data_inicio = models.DateField()
    data_fim = models.DateField()
    remuneracao = models.FloatField(null=True)
    descricao = models.CharField(max_length=500)

