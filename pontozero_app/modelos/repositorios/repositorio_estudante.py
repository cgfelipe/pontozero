from pontozero_app.modelos import BaseRepositorio
from pontozero_app.modelos import Estudante, Vaga


class RepositorioEstudante(BaseRepositorio):

    def cadastrar(self, estudante: Estudante):
        return estudante.save()

    def buscar(self, cpf):
        return Estudante.objects.get(cpf=cpf)

    def listar_todos(self):
        return Estudante.objects.all()

    def atualizar(self, cpf, **kwargs):
        modifiers = dict(**kwargs)
        for k, v in kwargs.items():
            if not hasattr(Estudante, k): del modifiers[k]
        estudante = Estudante.objects.filter(cpf=cpf)
        estudante.update(**modifiers)
        return estudante.first()

    def remover(self, **kwargs):
        estudante = Estudante.objects.get(**kwargs)
        if estudante:
            estudante.delete()

    def candidatar_a_vaga(self, estudante: Estudante, vaga: Vaga):
        vaga.estudantes.add(estudante)
        return vaga.save()
