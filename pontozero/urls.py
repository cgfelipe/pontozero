"""pontozero URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from pontozero_app.controllers import empresa_controller
from pontozero_app.controllers import estudante_controller
from pontozero_app.controllers import index_controller
from pontozero_app.controllers import IControleEstudante, IControleEmpresa, IControleVaga

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^$', index_controller.index, name='index'),

    url(r'^empresa/cadastrar/$', empresa_controller.CadastrarEmpresa.as_view(), name='cadastrar_empresa'),
    url(r'^empresa/visualizar/(?P<cnpj>\d+?)/$', empresa_controller.VisualizarEmpresa.as_view(), name='visualizar_empresa'),
    url(r'^empresa/todas/$', empresa_controller.ListarEmpresas.as_view(), name='listar_empresas'),

    url(r'^estudante/cadastrar/$', estudante_controller.CadastrarEstudante.as_view(), name='cadastrar_estudante'),
    url(r'^estudante/visualizar/(?P<cpf>\d+?)/$', estudante_controller.VisualizarEstudante.as_view(), name='visualizar_estudante'),
    url(r'^estudante/todos/$', estudante_controller.ListarEstudantes.as_view(), name='listar_estudantes'),

    url(r'^api/estudante/cadastrar/$', IControleEstudante.cadastrar, name='api_cadastrar_estudante'),
    url(r'^api/estudante/editar/$', IControleEstudante.editar, name='api_editar_estudante'),
    url(r'^api/estudante/visualizar/(?P<cpf>.+?)/$', IControleEstudante.visualizar, name='api_visualizar_estudante'),

    url(r'^api/estudante/vaga/candidatar/(?P<vaga_id>.+?)/', IControleVaga.candidatar_a_vaga, name='api_candidatar_vaga'),

    url(r'^api/empresa/cadastrar/', IControleEmpresa.cadastrar, name='api_cadastrar_empresa'),
    url(r'^api/empresa/editar/', IControleEmpresa.editar, name='api_editar_empresa'),
    url(r'api/empresa/visualizar/(?P<cnpj>.+?)/', IControleEmpresa.visualizar, name='api_visualizar_empresa'),

    url(r'^api/empresa/vaga/criar/', IControleVaga.criar, name='api_criar_vaga'),
    url(r'^api/empresa/vaga/fechar/(?P<vaga_id>.+?)/', IControleVaga.fechar, name='api_fechar_vaga'),
    url(r'^api/empresa/vaga/candidatos/(?P<vaga_id>.+?)/', IControleVaga.visualizar_candidatos, name='api_candidatos_vaga'),

    url(r'^api/vaga/visualizar/(?P<vaga_id>.+?)/', IControleVaga.visualizar, name='api_visualizar_vaga'),
    url(r'^api/vaga/buscar/', IControleVaga.buscar_vaga, name='api_buscar_vaga'),


]
