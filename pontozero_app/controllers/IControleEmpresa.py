from rest_framework.decorators import api_view
from rest_framework.response import Response
from pontozero_app.modelos import Empresa, Endereco, Fachada
from pontozero_app.controllers import utils
import json

fachada = Fachada.get_instance()


class IControleEmpresa(object):

    @staticmethod
    @api_view(['POST'])
    def cadastrar(request):
        endereco = Endereco(cep=request.data.get('cep'), rua=request.data.get('rua'),
                            bairro=request.data.get('bairro'), cidade=request.data.get('cidade'),
                            estado=request.data.get('estado'))
        empresa = Empresa(nome=request.data.get('nome'), ramo=request.data.get('ramo'), cnpj=request.data.get('cnpj'),
                          telefone=request.data.get('telefone'), email=request.data.get('email'),
                          site=request.data.get('site'), password=request.data.get('password'))
        fachada.cadastrar_empresa(empresa)
        endereco.save()
        fachada.atualizar_empresa(empresa.cnpj, endereco=endereco)
        return Response(
            "Empresa {} cadastrado com sucesso!".format(empresa.nome),
            status=200
        )

    @staticmethod
    @utils.login
    @utils.empresa_required
    @api_view(['POST'])
    def editar(request):
        cnpj, _ = utils.dumps_basic_auth(request.META['HTTP_AUTHORIZATION'])
        if cnpj != request.data.get('cnpj'):
            return Response("CNPJ difere do usuário autenticado")
        empresa_atual = fachada.buscar_empresa(cnpj=request.data.get('cnpj'))
        endereco = Endereco(cep=request.data.get('cep', empresa_atual.endereco.cep),
                            rua=request.data.get('rua', empresa_atual.endereco.rua),
                            bairro=request.data.get('bairro', empresa_atual.endereco.bairro),
                            cidade=request.data.get('cidade', empresa_atual.endereco.cidade),
                            estado=request.data.get('estado', empresa_atual.endereco.estado))
        endereco.save()
        modifiers = dict(request.data)
        if modifiers.get('cnpj'): del modifiers['cnpj']
        empresa = fachada.atualizar_empresa(cnpj=request.data.get('cnpj'), **modifiers, endereco=endereco)
        return Response(
            "Empresa {} editada com sucesso!".format(empresa.nome),
            status=200
        )


    @staticmethod
    @utils.login
    @api_view(['GET'])
    def visualizar(request, cnpj):
        empresa = fachada.buscar_empresa(cnpj=cnpj)
        return Response({
            'nome': empresa.nome,
            'cnpj': empresa.cnpj,
            'ramo': empresa.ramo,
            'email': empresa.email,
            'telefone': empresa.telefone,
            'site': empresa.site,
            'cidade': empresa.endereco.cidade,
            'estado': empresa.endereco.estado,
            'bairro': empresa.endereco.bairro,
            'rua': empresa.endereco.rua,
            'cep': empresa.endereco.cep
        }, status=200)
