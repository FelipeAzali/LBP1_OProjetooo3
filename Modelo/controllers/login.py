from flask import Flask, Blueprint, render_template, request, redirect, url_for, flash
from models import user, session

blueprint_login = Blueprint('login', __name__)

@blueprint_login.route('/login', methods=['POST', 'GET'])
def autenticar_usuario():
    if request.method == 'GET':
        if not session.exist('nome_usuario'):
            return render_template('login.html')
        else:
            return redirect(url_for('index'))
    
    if request.method == 'POST':
        nome_usuario = request.form['nome']
        senha_usuario = request.form['senha']
        
        usuario = user.autenticar(nome_usuario, senha_usuario)
        
        if usuario:
            session.iniciar_sessao('nome_usuario', nome_usuario)
            return redirect(url_for('dashboard'))
        else:
            flash('Nome de usuário ou senha incorretos!')
            return redirect(url_for('login'))

@blueprint_login.route('/logout')
def logout():
    session.limpar_login()
    return redirect(url_for('index'))
