from django.forms import ModelForm
from pontozero_app.modelos import Endereco


class EnderecoForm(ModelForm):

    class Meta:
        model = Endereco
        fields = '__all__'