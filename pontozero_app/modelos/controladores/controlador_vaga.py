from pontozero_app.modelos import CadastroVaga
from pontozero_app.modelos import RepositorioFactory

class ControladorVaga(object):
    cadastro_vaga = CadastroVaga(RepositorioFactory())

    def buscar(self, **kwargs):
        return self.cadastro_vaga.buscar(**kwargs)

    def listar_todas(self):
        return self.cadastro_vaga.listar_todos()
