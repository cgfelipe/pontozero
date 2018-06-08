from django.db import models
from pontozero_app.modelos.entidades.escola import Escola
from pontozero_app.modelos.entidades.pessoa import Pessoa
from werkzeug.security import check_password_hash, generate_password_hash
import base64


# Create your modelos here.


class Estudante(Pessoa):
    instituicao = models.ForeignKey(Escola, on_delete=models.CASCADE)

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
