from pontozero_app.modelos import ControladorEstudante, ControladorEmpresa, ControladorVaga
from pontozero_app.modelos import Empresa, Estudante, Vaga


class Fachada(object):

    __controlador_empresa = ControladorEmpresa()
    __controlador_estudante = ControladorEstudante()
    __controlador_vaga = ControladorVaga()


    @staticmethod
    def get_instance():
        return Fachada()

    def cadastrar_empresa(self, empresa):
        return self.__controlador_empresa.cadastrar(empresa)

    def buscar_empresa(self, cnpj):
        return self.__controlador_empresa.buscar(cnpj)

    def listar_todas_empresas(self):
        return self.__controlador_empresa.listar_todas()

    def atualizar_empresa(self, cnpj, **kwargs):
        return self.__controlador_empresa.atualizar(cnpj, **kwargs)

    def remover_empresa(self, **kwargs):
        self.__controlador_empresa.remover(**kwargs)

    def adicionar_vaga(self, empresa: Empresa, vaga: Vaga):
        return self.__controlador_empresa.adicionar_vaga(vaga, empresa)

    def buscar_vaga_empresa(self, empresa: Empresa, **kwargs):
        return self.__controlador_empresa.buscar_vaga(empresa, **kwargs)

    def buscar_vaga(self, **kwargs):
        return self.__controlador_vaga.buscar(**kwargs)

    def remover_vaga(self, empresa: Empresa, **kwargs):
        return self.__controlador_empresa.remover_vaga(empresa, **kwargs)

    def cadastrar_estudante(self, estudante):
        return self.__controlador_estudante.cadastrar(estudante)

    def buscar_estudante(self, cpf):
        return self.__controlador_estudante.buscar(cpf)

    def listar_todos_estudantes(self):
        return self.__controlador_estudante.listar_todos()

    def atualizar_estudante(self, cpf, **kwargs):
        return self.__controlador_estudante.atualizar(cpf, **kwargs)

    def remover_estudante(self, **kwargs):
        self.__controlador_estudante.remover(**kwargs)

    def candidatar_a_vaga(self, estudante, vaga):
        self.__controlador_estudante.candidatar_a_vaga(estudante, vaga)