from django.db import models
from pontozero_app.modelos import *


class Escola(Instituicao):
    cursos = models.ManyToManyField(Curso)
