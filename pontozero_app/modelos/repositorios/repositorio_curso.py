from pontozero_app.modelos import BaseRepositorio
from pontozero_app.modelos import Curso


class RepositorioCurso(BaseRepositorio):

    def cadastrar(self, curso: Curso):
        return curso.save()

    def buscar(self, identificador):
        return Curso.objects.get(identificador=identificador)

    def listar_todos(self):
        return Curso.objects.all()

    def atualizar(self, identificador, **kwargs):
        modifiers = dict(**kwargs)
        for k, v in kwargs.items():
            if not hasattr(Curso, k): del modifiers[k]
        curso = Curso.objects.filter(identificador=identificador)
        curso.update(**modifiers)
        return curso.first()

    def remover(self, **kwargs):
        curso = Curso.objects.get(**kwargs)
        if curso:
            curso.delete()
