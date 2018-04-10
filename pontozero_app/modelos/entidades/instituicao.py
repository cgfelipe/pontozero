from django.db import models
from pontozero_app.modelos import *


class Instituicao(models.Model):
    nome = models.CharField(max_length=200)
    cnpj = models.CharField(max_length=20, primary_key=True)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=20)
    endereco = models.OneToOneField(Endereco, null=True, on_delete=models.CASCADE)
    password = models.CharField(max_length=100)
    site = models.CharField(max_length=100)

