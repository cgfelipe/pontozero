from pontozero_app.modelos.cadastros.cadastro_instituicao import CadastroInstituicao

class CadastroEmpresa(CadastroInstituicao):

    def __init__(self, repositorio_factory):
        super(CadastroEmpresa, self).__init__(repositorio_factory, 'empresa')
