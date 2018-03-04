from pontozero_app.modelos import BaseRepositorio


class CadastroEstudante(object):
    repositorio = BaseRepositorio

    def __init__(self, repositorio_factory):
        self.repositorio = repositorio_factory.factory('estudante')

    def cadastrar(self, estudante):
        return self.repositorio.cadastrar(estudante)

    def buscar(self, cpf):
        return self.repositorio.buscar(cpf)

    def atualizar(self, cpf, **kwargs):
        return self.repositorio.atualizar(cpf, **kwargs)

    def remover(self, **kwargs):
        return self.repositorio.remover(**kwargs)

    def listar_todos(self):
        return self.repositorio.listar_todos()

    def candidatar_a_vaga(self, estudante, vaga):
        return self.repositorio.candidatar_a_vaga(estudante, vaga)
