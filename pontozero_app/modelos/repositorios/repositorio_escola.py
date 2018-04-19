from pontozero_app.modelos import BaseRepositorio
from pontozero_app.modelos import Escola, Vaga


class RepositorioEscola(BaseRepositorio):

    def cadastrar(self, escola: Escola):
        return escola.save()

    def buscar(self, cnpj):
        return Escola.objects.get(cnpj=cnpj)

    def listar_todos(self):
        return Escola.objects.all()

    def atualizar(self, cnpj, **kwargs):
        modifiers = dict(**kwargs)
        for k, v in kwargs.items():
            if not hasattr(Escola, k): del modifiers[k]
        escola = Escola.objects.filter(cnpj=cnpj)
        escola.update(**modifiers)
        return escola.first()

    def remover(self, **kwargs):
        escola = Escola.objects.get(**kwargs)
        if escola:
            escola.delete()

    def adicionar_vaga(self, vaga, escola):
        vaga.escola_responsavel = escola
        vaga.save()
        return vaga

    def remover_vaga(self, escola, **kwargs):
        vaga = Vaga.objects.get(escola_responsavel=escola, **kwargs)
        if vaga:
            vaga.delete()

    def buscar_vaga(self, escola, **kwargs):
        return Vaga.objects.get(escola_responsavel=escola, **kwargs)
