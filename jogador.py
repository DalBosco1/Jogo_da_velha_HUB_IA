class Jogador:
    contador_jogadores = 0  
    def __init__(self, simbolo):
        Jogador.contador_jogadores += 1
        self.nome = f"Player {Jogador.contador_jogadores}"
        self.simbolo = simbolo
        self.vitorias = 0

    def incrementar_vitorias(self):
        self.vitorias += 1