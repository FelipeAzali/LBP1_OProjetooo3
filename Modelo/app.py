from flask import Flask, render_template, session, request, redirect, url_for
from controllers import login, adm, carrinho
from models import session, items

aplicativo = Flask(__name__)
aplicativo.register_blueprint(login.c)
aplicativo.register_blueprint(adm.c)
aplicativo.register_blueprint(carrinho.c)
aplicativo.secret_key = 'senha super secreta'

@aplicativo.errorhandler(404)
def pagina_nao_encontrada(error):
    return 'Página não encontrada', 404

@aplicativo.errorhandler(401)
def acesso_proibido(error):
    return 'Acesso negado!', 401

@aplicativo.before_requisicao
def b4_requisicao():
    if requisicao.path == '/login':
        return
    if not session.existe('nome'):
        return redirecionar(url_para('login.login'))

@aplicativo.after_requisicao
def a_requisicao(response):
    print("Depois da requisição")
    return response

@aplicativo.route('/')
def index():
    carr = []
    for p in items.LISTA_PRODUTOS:
        cookie = requisicao.cookies.get(f'produto_{p.id}')
        if cookie:
            carr.append({
                'nome': p.nome,
                'qntd': cookie,
                'total': int(cookie)*p.preco
            })
    return renderizar_template('index.html', nome=session.get('nome'), produtos = items.LISTA_PRODUTOS, carrinho=carr)

if __name__ == '__main__':
    aplicativo.run(debug=True)
