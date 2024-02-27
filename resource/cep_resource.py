from flask import request
from flask_restful import Resource

from service.cep_service import CepService


class Cep(Resource):

    def get(self):
        cep = request.args.get('cep')
        cep = CepService.verifica_cep(cep)
        return cep, 200
