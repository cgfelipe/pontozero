from django.forms import ModelForm
from pontozero_app.modelos import Estudante


class EstudanteForm(ModelForm):

    class Meta:
        model = Estudante
        fields = ['nome', 'email', 'cpf', 'telefone', 'curriculo']
