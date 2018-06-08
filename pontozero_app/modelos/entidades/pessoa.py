from django.db import models
from pontozero_app.modelos.entidades.endereco import Endereco
# from pontozero_app.modelos.entidades.curriculo import Curriculo

class Pessoa(models.Model):
    nome = models.CharField(max_length=200)
    email = models.EmailField(primary_key=True)
    telefone = models.CharField(max_length=20)
    # curriculo = models.OneToOneField(Curriculo, on_delete=models.CASCADE)
    endereco = models.OneToOneField(Endereco, null=True, on_delete=models.CASCADE)
    password = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11, primary_key=True)

