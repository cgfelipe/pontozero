from pontozero_app.modelos import BaseRepositorio
from pontozero_app.modelos.cadastros.cadastro_pessoa import CadastroPessoa


class CadastroEstudante(CadastroPessoa):
    repositorio = BaseRepositorio

    def __init__(self, repositorio_factory):
        super(CadastroEstudante, self).__init__(repositorio_factory, 'estudante')

    def candidatar_a_vaga(self, estudante, vaga):
        return self.repositorio.candidatar_a_vaga(estudante, vaga)
