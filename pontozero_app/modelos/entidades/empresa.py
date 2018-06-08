from django.db import models
from pontozero_app.modelos import *
from werkzeug.security import check_password_hash, generate_password_hash
from django.core.validators import MaxValueValidator, MinValueValidator


class Empresa(Instituicao):
    ramo = models.CharField(max_length=200)
    reputacao = models.FloatField(default=5, validators=[MinValueValidator(0), MaxValueValidator(5)])

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
