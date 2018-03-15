import base64
from functools import wraps
from rest_framework.response import Response
from pontozero_app.modelos import Empresa, Estudante


def dumps_basic_auth(http_auth):
    auth = http_auth.split()
    if len(auth) == 2:
        # NOTE: We are only support basic authentication for now.
        #
        if auth[0].lower() == "basic":
            ident, password = base64.b64decode(auth[1]).decode('utf8').split(':')
            print(ident, password)
            return ident, password
    return None, None


def login(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        request = args[0]
        auth = request.META['HTTP_AUTHORIZATION']
        uname, password = dumps_basic_auth(auth)
        if uname and password:
            if Empresa.check_auth(uname, password) or Estudante.check_auth(uname, password):
                return f(*args, **kwargs)
        return Response("Autenticação inválida")
    return decorated


def estudante_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        request = args[0]
        auth = request.META['HTTP_AUTHORIZATION']
        uname, password = dumps_basic_auth(auth)
        if uname and password:
            if Estudante.check_auth(uname, password):
                return f(*args, **kwargs)
        return Response("Apenas estudantes podem executar esta ação")

    return decorated


def empresa_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        request = args[0]
        auth = request.META['HTTP_AUTHORIZATION']
        uname, password = dumps_basic_auth(auth)
        if uname and password:
            if Empresa.check_auth(uname, password):
                return f(*args, **kwargs)
        return Response("Apenas empresas podem executar esta ação")

    return decorated