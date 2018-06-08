from django.db import models
from pontozero_app.modelos.entidades.pessoa import Pessoa
from pontozero_app.modelos.entidades.escola import Escola

class Professor(Pessoa):
    disciplina = models.CharField(max_length=100)
    escola = models.ManyToManyField(Escola)
