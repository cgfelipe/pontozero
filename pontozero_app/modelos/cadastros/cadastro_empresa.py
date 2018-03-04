
class CadastroEmpresa(object):

    def __init__(self, repositorio_factory):
        self.repositorio = repositorio_factory.factory('empresa')

    def cadastrar(self, empresa):
        return self.repositorio.cadastrar(empresa)

    def buscar(self, cnpj):
        return self.repositorio.buscar(cnpj)

    def atualizar(self, cnpj, **kwargs):
        return self.repositorio.atualizar(cnpj, **kwargs)

    def remover(self, **kwargs):
        return self.repositorio.remover(**kwargs)

    def adicionar_vaga(self, vaga, empresa):
        return self.repositorio.adicionar_vaga(vaga, empresa)

    def remover_vaga(self, empresa, **kwargs):
        return self.repositorio.remover_vaga(empresa, **kwargs)

    def buscar_vaga(self, empresa, **kwargs):
        return self.repositorio.buscar_vaga_empresa(empresa, **kwargs)

    def listar_todas(self):
        return self.repositorio.listar_todos()