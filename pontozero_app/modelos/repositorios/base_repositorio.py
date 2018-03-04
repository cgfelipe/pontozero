
class BaseRepositorio(object):

    repositorio_id = ''

    def __new__(cls, *args, **kwargs):
        obj = super(BaseRepositorio, cls).__new__(cls)
        obj.repositorio_id = obj.__class__.__name__.lower()
        return obj

    def cadastrar(self, *args, **kwargs):
        pass

    def buscar(self, *args, **kwargs):
        pass

    def listar_todos(self, *args, **kwargs):
        pass

    def atualizar(self, *args, **kwargs):
        pass

    def remover(self, *args, **kwargs):
        pass