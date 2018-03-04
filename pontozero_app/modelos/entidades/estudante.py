from django.db import models
from pontozero_app.modelos import *
from werkzeug.security import check_password_hash, generate_password_hash
import base64


# Create your modelos here.


class Estudante(models.Model):
    nome = models.CharField(max_length=200)
    cpf = models.CharField(max_length=11, primary_key=True)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=20)
    curriculo = models.FileField(null=True, blank=True)
    endereco = models.OneToOneField(Endereco, null=True)
    password = models.CharField(max_length=100)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.password = generate_password_hash(self.password)
        super(Estudante, self).save(force_insert=force_insert, force_update=force_update,
                                    using=using, update_fields=update_fields)

    @staticmethod
    def check_auth(cpf, password):
        estudante = Estudante.objects.filter(cpf=cpf)
        if estudante:
            return check_password_hash(estudante[0].password, password)
        return False
