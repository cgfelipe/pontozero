from pontozero_app.modelos import BaseRepositorio
from pontozero_app.modelos import Empresa, Vaga


class RepositorioEmpresa(BaseRepositorio):

    def cadastrar(self, empresa: Empresa):
        return empresa.save()

    def buscar(self, cnpj):
        return Empresa.objects.get(cnpj=cnpj)

    def listar_todos(self):
        return Empresa.objects.all()

    def atualizar(self, cnpj, **kwargs):
        modifiers = dict(**kwargs)
        for k, v in kwargs.items():
            if not hasattr(Empresa, k): del modifiers[k]
        empresa = Empresa.objects.filter(cnpj=cnpj)
        empresa.update(**modifiers)
        return empresa.first()

    def remover(self, **kwargs):
        empresa = Empresa.objects.get(**kwargs)
        if empresa:
            empresa.delete()

    def adicionar_vaga(self, vaga, empresa):
        vaga.empresa_responsavel = empresa
        vaga.save()
        return vaga

    def remover_vaga(self, empresa, **kwargs):
        vaga = Vaga.objects.get(empresa_responsavel=empresa, **kwargs)
        if vaga:
            vaga.delete()

    def buscar_vaga(self, empresa, **kwargs):
        return Vaga.objects.get(empresa_responsavel=empresa, **kwargs)
