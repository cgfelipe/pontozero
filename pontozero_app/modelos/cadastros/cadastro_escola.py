from pontozero_app.modelos import CadastroInstituicao


class CadastroEmpresa(CadastroInstituicao):

    def __init__(self, repositorio_factory):
        super(CadastroEmpresa, self).__init__(repositorio_factory, 'escola')
