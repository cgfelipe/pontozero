from django.db import models
from pontozero_app.modelos import *


class Professor(Pessoa):
    disciplina = models.CharField(max_length=100)
    escola = models.ManyToManyField(Escola)
