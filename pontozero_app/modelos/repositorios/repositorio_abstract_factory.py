from pontozero_app.modelos import (
    RepositorioEmpresa,
    RepositorioEstudante,
    RepositorioVaga,
    RepositorioEscola,
    RepositorioProfessor,
    RepositorioTrabalho,
    RepositorioCurso,
    RepositorioCurriculo,
)


class RepositorioFactory(object):

    @staticmethod
    def factory(_type):
        if 'empresa' in _type:
            return RepositorioEmpresa()
        elif 'escola' in _type:
            return RepositorioEscola()
        elif 'estudante' in _type:
            return RepositorioEstudante()
        elif 'professor' in _type:
            return RepositorioProfessor()
        elif 'vaga' in _type:
            return RepositorioVaga()
        elif 'trabalho' in _type:
            return RepositorioTrabalho()
        elif 'curso' in _type:
            return RepositorioCurso()
        elif 'curriculo' in _type:
            return RepositorioCurriculo()
        raise Exception('Invalid type ' + _type)
