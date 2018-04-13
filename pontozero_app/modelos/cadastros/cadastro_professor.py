from pontozero_app.modelos import BaseRepositorio
from pontozero_app.modelos import CadastroPessoa


class CadastroEstudante(CadastroPessoa):
    repositorio = BaseRepositorio

    def __init__(self, repositorio_factory):
        super(CadastroEstudante, self).__init__(repositorio_factory, 'estudante')
