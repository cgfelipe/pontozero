from pontozero_app.modelos import BaseRepositorio
from pontozero_app.modelos import Trabalho


class RepositorioTrabalho(BaseRepositorio):

    def cadastrar(self, trabalho: Trabalho):
        return trabalho.save()

    def buscar(self, identificador):
        return Trabalho.objects.get(identificador=identificador)

    def listar_todos(self):
        return Trabalho.objects.all()

    def atualizar(self, identificador, **kwargs):
        modifiers = dict(**kwargs)
        for k, v in kwargs.items():
            if not hasattr(Trabalho, k): del modifiers[k]
        trabalho = Trabalho.objects.filter(identificador=identificador)
        trabalho.update(**modifiers)
        return trabalho.first()

    def remover(self, **kwargs):
        trabalho = Trabalho.objects.get(**kwargs)
        if trabalho:
            trabalho.delete()
