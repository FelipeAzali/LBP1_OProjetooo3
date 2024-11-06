class Usuario:
    def __init__(self, nome, senha, tipo):
        self.nome = nome
        self.senha = senha
        self.tipo = tipo

USUARIOS = [
    Usuario("Administrador", '123', 'admin'),
    Usuario("Glauber", '321', 'padrao')
]