from django.db import models
from pontozero_app.modelos.entidades.trabalho import Trabalho
from pontozero_app.modelos.entidades.curso import Curso


class Curriculo(models.Model):
    cursos = models.ManyToManyField(Curso)
    trabalhos = models.ManyToManyField(Trabalho)
    objetivo = models.CharField(max_length=500)
