import requests

from enuns.menssage_enum import CepMessagem
from variaveis.variaveis import URL_VIA_CEP, FORMATO_JSON


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
            cep = [requisicao.json() if requisicao.json() else None]
            verifica = cep[0].get('erro', None)
            if verifica:
                return {
                    'message': CepMessagem.MENSAGEM_RETORNO_NONE.value
                }
            return {
                'cep': str(cep[0]['cep']),
                'logradouro': str(cep[0]['logradouro']),
                'bairro': str(cep[0]['bairro']),
                'uf': str(cep[0]['uf']),
                'ddd': str(cep[0]['ddd'])
            }
        else:
            return {
                'message': CepMessagem.MENSAGEM_RETORNO_500.value
            }
