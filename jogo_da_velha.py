class JogoDaVelha:
    def __init__(self, jogador1, jogador2):
        self.jogador1 = jogador1
        self.jogador2 = jogador2
        self.tabuleiro = [str(i) for i in range(1, 10)]
        self.jogador_atual = None 

    def mostrar_tabuleiro(self):
        print('\n')
        print('Jogo da Velha ')
        print('\n')
        print(f' {self.tabuleiro[0]} | {self.tabuleiro[1]} | {self.tabuleiro[2]} ')
        print('---+---+---')
        print(f' {self.tabuleiro[3]} | {self.tabuleiro[4]} | {self.tabuleiro[5]} ')
        print('---+---+---')
        print(f' {self.tabuleiro[6]} | {self.tabuleiro[7]} | {self.tabuleiro[8]} ')
        print('\n')

    def fazer_jogada(self, posicao, simbolo):
        index = posicao - 1
        
        if index < 0 or index > 8:
            return False  
        
        # se já jogado 
        if self.tabuleiro[index] not in ['O', 'X']:
            self.tabuleiro[index] = simbolo
            return True
        
        return False

    def verificar_vencedor(self, simbolo):
        
        """define quais posiçoes ganham"""
        
        combos = [(0, 1, 2), (3, 4, 5), (6, 7, 8),  (0, 3, 6), (1, 4, 7), (2, 5, 8),  (0, 4, 8), (2, 4, 6)]
        
        for a, b, c in combos:
            if self.tabuleiro[a] == simbolo and self.tabuleiro[b] == simbolo and self.tabuleiro[c] == simbolo:
                return True
        return False

    def tabuleiro_cheio(self):
        return all(celula in ['O', 'X'] for celula in self.tabuleiro)

    def trocar_jogador(self):
        
        if self.jogador_atual == self.jogador1:
            self.jogador_atual = self.jogador2
        else:
            self.jogador_atual = self.jogador1

    def reiniciar_tabuleiro(self):
        self.tabuleiro = [str(i) for i in range(1, 10)]
