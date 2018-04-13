
class CadastroInstituicao(object):

    def __init__(self, repositorio_factory, tipo_instituicao):
        self.repositorio = repositorio_factory.factory(tipo_instituicao)

    def cadastrar(self, instituicao):
        return self.repositorio.cadastrar(instituicao)

    def buscar(self, cnpj):
        return self.repositorio.buscar(cnpj)

    def atualizar(self, cnpj, **kwargs):
        return self.repositorio.atualizar(cnpj, **kwargs)

    def remover(self, **kwargs):
        return self.repositorio.remover(**kwargs)

    def adicionar_vaga(self, vaga, instituicao):
        return self.repositorio.adicionar_vaga(vaga, instituicao)

    def remover_vaga(self, instituicao, **kwargs):
        return self.repositorio.remover_vaga(instituicao, **kwargs)

    def buscar_vaga(self, instituicao, **kwargs):
        return self.repositorio.buscar_vaga_instituicao(instituicao, **kwargs)

    def listar_todas(self):
        return self.repositorio.listar_todos()