from flask import Flask, render_template, session, request, redirect, url_for
from controllers import login, adm, carrinho
from models import session, items

app = Flask(__name__)
app.register_blueprint(login.c)
app.register_blueprint(adm.c)
app.register_blueprint(carrinho.c)
app.secret_key = 'senha super secreta'

@app.errorhandler(404)
def pagina_nao_encontrada(error):
    return 'Página não encontrada', 404

@app.errorhandler(401)
def acesso_proibido(error):
    return 'Acesso negado!', 401

@app.before_requisicao
def b4_requisicao():
    if request.path == '/login':
        return
    if not session.existe('nome'):
        return redirect(url_for('login.login'))

@app.after_requisicao
def a_requisicao(response):
    print("Depois da requisição")
    return response

@app.route('/')
def index():
    carr = []
    for p in items.LISTA_PRODUTOS:
        cookie = request.cookies.get(f'produto_{p.id}')
        if cookie:
            carr.append({
                'nome': p.nome,
                'qntd': cookie,
                'total': int(cookie)*p.preco
            })
    return render_template('index.html', nome=session.get('nome'), produtos = items.LISTA_PRODUTOS, carrinho=carr)

if __name__ == '__main__':
    app.run(debug=True)
