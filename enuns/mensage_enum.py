from enum import Enum


class CepMessagem(Enum):
    MENSAGEM_RETORNO_500 = 'Ocorreu um erro na integração'
    MENSAGEM_RETORNO_NONE = 'Não foi possivel verificar o cep solicitado'
