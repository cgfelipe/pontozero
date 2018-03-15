from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.views import View
from pontozero_app.modelos import EmpresaForm, EnderecoForm
from pontozero_app.modelos import Fachada
from django.contrib import messages


fachada = Fachada.get_instance()


class CadastrarEmpresa(View):

    def get(self, request):
        form = EmpresaForm()
        endereco_form = EnderecoForm()
        return render(request, 'cadastro-empresa.html', locals())

    def post(self, request):
        form = EmpresaForm(request.POST)
        endereco_form = EnderecoForm(request.POST)
        if form.is_valid() and endereco_form.is_valid():
            endereco = endereco_form.save()
            empresa = fachada.cadastrar_empresa(form)
            fachada.atualizar_empresa(empresa.cnpj, endereco=endereco)
            messages.success(request, 'Empresa {} cadastrada com sucesso!'.format(empresa.nome))
            return redirect(reverse('index'))
        if form.errors: messages.error(request, form.errors)
        if endereco_form.errors: messages.error(request, endereco_form.errors)
        return redirect(reverse('cadastrar_empresa'))


class VisualizarEmpresa(View):

    def get(self, request, cnpj):
        empresa = fachada.buscar_empresa(cnpj)
        form = EmpresaForm(instance=empresa)
        endereco_form = EnderecoForm(instance=empresa.endereco)
        return render(request, 'visualizar-empresa.html', locals())

    def post(self, request, cnpj):
        if request.POST.get('atualizar'):
            return self.atualizar_empresa(request, cnpj)
        else:
            return self.deletar_empresa(request, cnpj)

    def deletar_empresa(self, request, cnpj):
        fachada.remover_empresa(cnpj=cnpj)
        messages.success(request, 'Empresa removida com sucesso')
        return redirect(reverse('listar_empresas'))

    def atualizar_empresa(self, request, cnpj):
        endereco_form = EnderecoForm(request.POST)
        endereco = endereco_form.save()
        fachada.atualizar_empresa(cnpj, nome=request.POST['nome'], email=request.POST['email'],
                                    telefone=request.POST['telefone'], site=request.POST['site'],
                                    endereco=endereco, ramo=request.POST['ramo'])
        messages.success(request, 'Empresa atualizada com sucesso')
        return redirect(reverse('visualizar_empresa', kwargs={'cnpj': cnpj}))



class ListarEmpresas(View):
    def get(self, request):
        empresas = fachada.listar_todas_empresas()
        return render(request, 'lista-empresas.html', locals())