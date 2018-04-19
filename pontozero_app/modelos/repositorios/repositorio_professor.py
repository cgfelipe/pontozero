from pontozero_app.modelos import BaseRepositorio
from pontozero_app.modelos import Professor, Vaga


class RepositorioProfessor(BaseRepositorio):

    def cadastrar(self, professor: Professor):
        return professor.save()

    def buscar(self, cpf):
        return Professor.objects.get(cpf=cpf)

    def listar_todos(self):
        return Professor.objects.all()

    def atualizar(self, cpf, **kwargs):
        modifiers = dict(**kwargs)
        for k, v in kwargs.items():
            if not hasattr(Professor, k): del modifiers[k]
        professor = Professor.objects.filter(cpf=cpf)
        professor.update(**modifiers)
        return professor.first()

    def remover(self, **kwargs):
        professor = Professor.objects.get(**kwargs)
        if professor:
            professor.delete()

    def candidatar_a_vaga(self, professor: Professor, vaga: Vaga):
        vaga.professors.add(professor)
        return vaga.save()
