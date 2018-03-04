from pontozero_app.modelos import RepositorioEmpresa, RepositorioEstudante, RepositorioVaga


class RepositorioFactory(object):

    @staticmethod
    def factory(_type):
        if 'empresa' in _type:
            return RepositorioEmpresa()
        elif 'estudante' in _type:
            return RepositorioEstudante()
        elif 'vaga' in _type:
            return RepositorioVaga()
        raise Exception('Invalid type ' + _type)