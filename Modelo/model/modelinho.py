class Jogador:
   def __init__(self, id, nome, pais, categoria, video):
       self.id = id
       self.nome = nome
       self.pais = pais
       self.categoria = categoria
       self.video = video


jogadores = []

Players = Jogador(1, "nome", "Brasil", "Any%", "link")

jogadores.append(Players)