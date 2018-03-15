from pontozero_app.controllers import utils
from pontozero_app.modelos import Vaga, Fachada
from rest_framework.decorators import api_view
from rest_framework.response import Response
import json
import datetime

fachada = Fachada.get_instance()


class IControleVaga(object):
    @staticmethod
    @utils.login
    @utils.empresa_required
    @api_view(['POST'])
    def criar(request):
        cnpj, _ = utils.dumps_basic_auth(request.META['HTTP_AUTHORIZATION'])
        if request.data.get('empresa_responsavel') != cnpj:
            Response("Você não tem autorização para criar uma vaga para outra empresa")
        empresa_responsavel = fachada.buscar_empresa(cnpj=request.data.get('empresa_responsavel'))
        data_abertura = datetime.datetime.now()
        vaga = Vaga(
            nome=request.data.get('nome'), data_abertura=data_abertura,
            setor=request.data.get('setor'), funcao=request.data.get('funcao'),
            descricao=request.data.get('descricao')
        )
        vaga = fachada.adicionar_vaga(empresa_responsavel, vaga)
        return Response(
            "Vaga {} criada com sucesso, ID={}!".format(vaga.nome, vaga.id),
            status=200
        )

    @staticmethod
    @utils.login
    @utils.empresa_required
    @api_view(['POST'])
    def fechar(request, vaga_id):
        cnpj, _ = utils.dumps_basic_auth(request.META['HTTP_AUTHORIZATION'])
        empresa_responsavel = fachada.buscar_empresa(cnpj)
        fachada.remover_vaga(empresa=empresa_responsavel, id=vaga_id)
        return Response(
            "Vaga removida com sucesso",
            status=200
        )

    @staticmethod
    @api_view(['GET'])
    def visualizar(request, vaga_id):
        vaga = Vaga.objects.get(id=vaga_id)
        return Response(
            json.dumps({
                'nome': vaga.nome,
                'id': vaga.id,
                'data_abertura': str(vaga.data_abertura),
                'setor': vaga.setor,
                'funcao': vaga.funcao,
                'descricao': vaga.descricao,
                'empresa_responsavel': vaga.empresa_responsavel.nome
            }),
            status=200
        )

    @staticmethod
    @utils.login
    @utils.empresa_required
    @api_view(['GET'])
    def visualizar_candidatos(request, vaga_id):
        cnpj, _ = utils.dumps_basic_auth(request.META['HTTP_AUTHORIZATION'])
        empresa_responsavel = fachada.buscar_empresa(cnpj)
        vaga = fachada.buscar_vaga_empresa(empresa_responsavel, id=vaga_id)
        candidatos = vaga.estudantes
        return Response(json.dumps([{
            'nome': c.nome,
            'cpf': c.cpf
        } for c in candidatos]),
            status=200
        )

    @staticmethod
    @utils.login
    @api_view(['POST'])
    def buscar_vaga(request):
        vagas = Vaga.objects.filter(**request.data)
        return Response(json.dumps({
                'nome': vaga.nome,
                'id': vaga.id,
                'data_abertura': str(vaga.data_abertura),
                'setor': vaga.setor,
                'funcao': vaga.funcao,
                'descricao': vaga.descricao,
                'empresa_responsavel': vaga.empresa_responsavel.nome
            }) for vaga in vagas)

    @staticmethod
    @utils.login
    @utils.estudante_required
    @api_view(['POST'])
    def candidatar_a_vaga(request, vaga_id):
        cpf, _ = utils.dumps_basic_auth(request.META['HTTP_AUTHORIZATION'])
        estudante = fachada.buscar_estudante(cpf)
        vaga = fachada.buscar_vaga(id=vaga_id)
        fachada.candidatar_a_vaga(estudante, vaga)
        return Response("Estudante {} candidatou-se com sucesso a vaga de {}".format(estudante.nome, vaga.nome),
                        status=200)
