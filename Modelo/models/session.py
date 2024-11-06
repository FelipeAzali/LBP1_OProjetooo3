from flask import session as sessao

DADOS_LOGIN = ['usuario_nome', 'usuario_tipo']

def campo_existe(chave):
    return chave in sessao

def obter_valor(chave):
    return sessao[chave]

def atualizar_valor(chave, valor_novo):
    sessao[chave] = valor_novo

def limpar_sessao():
    for chave in DADOS_LOGIN:
        sessao.pop(chave, None)