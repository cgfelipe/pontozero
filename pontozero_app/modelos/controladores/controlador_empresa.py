from pontozero_app.modelos import CadastroEmpresa
from pontozero_app.modelos import RepositorioFactory


class ControladorEmpresa(object):
    cadastro_empresa = CadastroEmpresa(RepositorioFactory())

    def cadastrar(self, empresa):
        return self.cadastro_empresa.cadastrar(empresa)

    def buscar(self, cnpj):
        return self.cadastro_empresa.buscar(cnpj)

    def listar_todas(self):
        return self.cadastro_empresa.listar_todas()

    def atualizar(self, cnpj, **kwargs):
        return self.cadastro_empresa.atualizar(cnpj, **kwargs)

    def remover(self, **kwargs):
        return self.cadastro_empresa.remover(**kwargs)

    def adicionar_vaga(self, vaga, empresa):
        return self.cadastro_empresa.adicionar_vaga(vaga, empresa)

    def buscar_vaga(self, empresa, **kwargs):
        return self.cadastro_empresa.buscar_vaga(empresa, **kwargs)

    def remover_vaga(self, empresa, **kwargs):
        return self.cadastro_empresa.remover_vaga(empresa, **kwargs)


    # def listar_vagas_da_empresa(self):
    #     return Vaga.objects.get(empresa_responsavel=self.empresa)

    # @staticmethod
    # def listar_vagas():
    #     return Vaga.objects.all()
