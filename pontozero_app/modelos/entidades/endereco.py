from django.db import models


class Endereco(models.Model):
    cep = models.BigIntegerField(max_length=8)
    rua = models.CharField(max_length=200)
    bairro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)

