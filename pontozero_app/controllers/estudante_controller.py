from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.views import View
from pontozero_app.modelos import EstudanteForm, EnderecoForm, Fachada
from django.contrib import messages

fachada = Fachada.get_instance()


class CadastrarEstudante(View):
    def get(self, request):
        form = EstudanteForm()
        endereco_form = EnderecoForm()
        return render(request, 'cadastro-estudante.html', locals())

    def post(self, request):
        form = EstudanteForm(request.POST)
        endereco_form = EnderecoForm(request.POST)
        if form.is_valid() and endereco_form.is_valid():
            endereco = endereco_form.save()
            estudante = fachada.cadastrar_estudante(form)
            fachada.atualizar_estudante(estudante.cpf, endereco=endereco)
            messages.success(request, 'Estudante {} cadastrado com sucesso!'.format(estudante.nome))
            return redirect(reverse('listar_estudantes'))
        if form.errors: messages.error(request, form.errors)
        if endereco_form.errors: messages.error(request, endereco_form.errors)
        return redirect(reverse('cadastrar_estudante'))


class VisualizarEstudante(View):
    def get(self, request, cpf):
        estudante = fachada.buscar_estudante(cpf)
        form = EstudanteForm(instance=estudante)
        endereco_form = EnderecoForm(instance=estudante.endereco)
        return render(request, 'visualizar-estudante.html', locals())

    def post(self, request, cpf):
        if request.POST.get('atualizar'):
            return self.atualizar_estudante(request, cpf)
        else:
            return self.deletar_estudante(request, cpf)

    def deletar_estudante(self, request, cpf):
        fachada.remover_estudante(cpf=cpf)
        messages.success(request, 'Estudante removido com sucesso')
        return redirect(reverse('listar_estudantes'))

    def atualizar_estudante(self, request, cpf):
        endereco_form = EnderecoForm(request.POST)
        endereco = endereco_form.save()
        fachada.atualizar_estudante(cpf, nome=request.POST['nome'], email=request.POST['email'],
                                    telefone=request.POST['telefone'], curriculo=request.POST['curriculo'],
                                    endereco=endereco)
        messages.success(request, 'Estudante atualizado com sucesso')
        return redirect(reverse('visualizar_estudante', kwargs={'cpf': cpf}))


class ListarEstudantes(View):
    def get(self, request):
        estudantes = fachada.listar_todos_estudantes()
        return render(request, 'lista-estudantes.html', locals())