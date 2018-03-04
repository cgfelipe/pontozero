from pontozero_app.modelos import BaseRepositorio
from pontozero_app.modelos import Estudante, Vaga


class RepositorioVaga(BaseRepositorio):

    def buscar(self, **kwargs):
        return Vaga.objects.get(**kwargs)

    def listar_todos(self):
        return Vaga.objects.all()

    def remover(self, **kwargs):
        estudante = Estudante.objects.get(**kwargs)
        if estudante:
            estudante.delete()
