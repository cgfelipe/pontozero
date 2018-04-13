from pontozero_app.modelos import BaseRepositorio


class CadastroPessoa(object):
    repositorio = BaseRepositorio

    def __init__(self, repositorio_factory, tipo_pessoa):
        self.repositorio = repositorio_factory.factory(tipo_pessoa)

    def cadastrar(self, pessoa):
        return self.repositorio.cadastrar(pessoa)

    def buscar(self, cpf):
        return self.repositorio.buscar(cpf)

    def atualizar(self, cpf, **kwargs):
        return self.repositorio.atualizar(cpf, **kwargs)

    def remover(self, **kwargs):
        return self.repositorio.remover(**kwargs)

    def listar_todos(self):
        return self.repositorio.listar_todos()
