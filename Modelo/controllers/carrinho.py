from flask import Flask, Blueprint, render_template, request, redirect, url_for, make_response, flash
from models import items

c = Blueprint('carrinho', __name__)

@c.route('/carrinho/add') # type: ignore
def adicionar_ao_carrinho():
    if 'produto_id' in request.form:
        produto_id = request.form['produto_id']
        # Outras operações...
    return redirect(url_for('carrinho.exibir'))

@c.route('/carrinho/del')
def delete():
    id = request.args.get('id')
    resp = make_response(redirect(url_for('index')))
    cookie = request.cookies.get(f'produto_{id}')
    if cookie:
        if int(cookie)-1 > 0:
            resp.set_cookie(f'produto_{id}', str(int(cookie)-1))
        else:
            resp.set_cookie(f'produto_{id}', '0', expires=0)
    else:
        flash('O produto não pode ser removido.', 'warning')
    return resp
