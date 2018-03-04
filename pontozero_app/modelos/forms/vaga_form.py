from django.forms import ModelForm
from pontozero_app.modelos import Vaga


class VagaForm(ModelForm):

    class Meta:
        model = Vaga
        fields = '__all__'
