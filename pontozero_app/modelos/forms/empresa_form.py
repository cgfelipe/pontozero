from django.forms import ModelForm
from pontozero_app.modelos import Empresa


class EmpresaForm(ModelForm):

    class Meta:
        model = Empresa
        fields = ['nome', 'email', 'cnpj', 'ramo', 'telefone', 'site']


