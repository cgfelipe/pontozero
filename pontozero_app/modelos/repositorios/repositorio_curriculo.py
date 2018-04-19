from pontozero_app.modelos import BaseRepositorio
from pontozero_app.modelos import Curriculo


class RepositorioCurriculo(BaseRepositorio):

    def cadastrar(self, curriculo: Curriculo):
        return curriculo.save()

    def buscar(self, identificador):
        return Curriculo.objects.get(identificador=identificador)

    def listar_todos(self):
        return Curriculo.objects.all()

    def atualizar(self, identificador, **kwargs):
        modifiers = dict(**kwargs)
        for k, v in kwargs.items():
            if not hasattr(Curriculo, k): del modifiers[k]
        curriculo = Curriculo.objects.filter(identificador=identificador)
        curriculo.update(**modifiers)
        return curriculo.first()

    def remover(self, **kwargs):
        curriculo = Curriculo.objects.get(**kwargs)
        if curriculo:
            curriculo.delete()
