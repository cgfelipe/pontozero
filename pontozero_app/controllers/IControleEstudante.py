from rest_framework.decorators import api_view
from rest_framework.response import Response
from pontozero_app.modelos import Estudante, Endereco, Fachada
from pontozero_app.controllers import utils


fachada = Fachada.get_instance()


class IControleEstudante(object):

    @staticmethod
    @api_view(['POST'])
    def cadastrar(request):
        endereco = Endereco(cep=request.data.get('cep'), rua=request.data.get('rua'),
                            bairro=request.data.get('bairro'), cidade=request.data.get('cidade'),
                            estado=request.data.get('estado'))
        endereco.save()
        estudante = Estudante(nome=request.data.get('nome'), cpf=request.data.get('cpf'),
                              email=request.data.get('email'), telefone=request.data.get('telefone'),
                              password=request.data.get('password'))
        fachada.cadastrar_estudante(estudante)
        fachada.atualizar_estudante(estudante.cpf, endereco=endereco)
        return Response(
            "Estudante {} cadastrado com sucesso!".format(estudante.nome),
            status=200
        )

    @staticmethod
    @utils.login
    @utils.estudante_required
    @api_view(['POST'])
    def editar(request):
        cpf, _ = utils.dumps_basic_auth(request.META['HTTP_AUTHORIZATION'])
        if cpf != request.data.get('cpf'):
            return Response("CPF difere do usuário autenticado")
        estudante_atual = fachada.buscar_estudante(cpf=request.data.get('cpf'))
        endereco = Endereco(cep=request.data.get('cep', estudante_atual.endereco.cep),
                            rua=request.data.get('rua', estudante_atual.endereco.rua),
                            bairro=request.data.get('bairro', estudante_atual.endereco.bairro),
                            cidade=request.data.get('cidade', estudante_atual.endereco.cidade),
                            estado=request.data.get('estado', estudante_atual.endereco.estado))
        endereco.save()
        modifiers = dict(request.data)
        if modifiers.get('cpf'):
            del modifiers['cpf']
        estudante = fachada.atualizar_estudante(cpf=request.data.get('cpf'), **modifiers)
        return Response(
            "Estudante {} editado com sucesso!".format(estudante.nome),
            status=200
        )


    @staticmethod
    @utils.login
    @api_view(['GET'])
    def visualizar(request, cpf):
        estudante = fachada.buscar_estudante(cpf=cpf)
        return Response({
            'nome': estudante.nome,
            'cpf': estudante.cpf,
            'telefone': estudante.telefone,
            'email': estudante.email,
            'cep': estudante.endereco.cep,
        })