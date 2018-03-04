from django.db import models
from pontozero_app.modelos import *
from werkzeug.security import check_password_hash, generate_password_hash


class Empresa(models.Model):
    nome = models.CharField(max_length=200)
    ramo = models.CharField(max_length=200)
    cnpj = models.CharField(max_length=20, primary_key=True)
    telefone = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    site = models.CharField(max_length=100)
    endereco = models.OneToOneField(Endereco, null=True)
    password = models.CharField(max_length=100)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.password = generate_password_hash(self.password)
        super(Empresa, self).save(force_insert=force_insert, force_update=force_update,
                                    using=using, update_fields=update_fields)

    @staticmethod
    def check_auth(cnpj, password):
        empresa = Empresa.objects.filter(cnpj=cnpj)
        if empresa:
            return check_password_hash(empresa[0].password, password)
        return False

    def __str__(self):
        return '{} - {}'.format(self.nome, self.cnpj)
