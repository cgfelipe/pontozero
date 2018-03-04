from pontozero_app.modelos import BaseRepositorio


class CadastroVaga(object):
    repositorio = BaseRepositorio

    def __init__(self, repositorio_factory):
        self.repositorio = repositorio_factory.factory('vaga')

    def buscar(self, **kwargs):
        return self.repositorio.buscar(**kwargs)

    def listar_todos(self):
        return self.repositorio.listar_todos()

    def candidatar_a_vaga(self, estudante, vaga):
        return self.repositorio.candidatar_a_vaga(estudante, vaga)
