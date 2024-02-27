import requests

from variaveis.variaveis import URL_VIA_CEP, FORMATO_JSON
from enuns.menssage_enum import CepMessagem

class CepService:
    @classmethod
    def verifica_cep(cls, cep):
        cep = cls.formata_cep(cep)
        cep = cls.chama_requisicao(cep)
        return cep

    @classmethod
    def formata_cep(cls, cep):
        cep = cep.replace("-", "")
        cep = cep.replace(" ", "")
        cep = cep.replace(".", "")
        return int(cep)

    @classmethod
    def chama_requisicao(cls, cep):
        URL = f'{URL_VIA_CEP}{cep}{FORMATO_JSON}'
        requisicao = requests.get(URL)
        if requisicao.status_code == 200:
            cep = requisicao.json() if requisicao.json() else None
            verifica = cep['erro']
            if verifica:
                return {
                    'message': CepMessagem.MENSAGEM_RETORNO_NONE
                }
            return {
                'cep': cep['cep'],
                'logradouro': cep['logradouro'],
                'bairro': cep['bairro'],
                'uf': cep['uf'],
                'ddd': cep['ddd']
            } , 200
