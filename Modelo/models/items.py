class Produto:
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price

LISTA_PRODUTOS = [
    Produto(1, 'Arroz', 22),
    Produto(2, 'Feijão', 15),
    Produto(3, 'Batata', 10)
]
