import random
from jogador import Jogador
from jogo_da_velha import JogoDaVelha

def main():
    print('Bem-vindo ao Jogo da Velha!\n')
    jogador1 = Jogador('O')
    jogador2 = Jogador('X')
    jogo = JogoDaVelha(jogador1, jogador2)

    jogo.jogador_atual = random.choice([jogador1, jogador2])
    print(f'\n{jogo.jogador_atual.nome} começa o jogo!')

    input("Pressione Enter para começar ")



    while Tr
        print('Jogo da velha')
        jogo.mostrar_tabuleiro()

        try:
            posicao = int(input(f'{jogo.jogador_atual.nome} ({jogo.jogador_atual.simbolo}), escolha uma posição (1-9): '))
        except ValueError:
            print('Entrada inválida. Digite um número de 1 a 9.')
            continue

        if jogo.fazer_jogada(posicao, jogo.jogador_atual.simbolo):
            if jogo.verificar_vencedor(jogo.jogador_atual.simbolo):
                
                jogo.mostrar_tabuleiro()
                print(f'\n{jogo.jogador_atual.nome} venceu!\n')
                jogo.jogador_atual.incrementar_vitorias()
                print(f'Placar: {jogador1.nome} ({jogador1.vitorias} x {jogador2.vitorias}) {jogador2.nome}')

                if input('Jogar novamente? (s/n): ').lower() != 's':
                    break

                jogo.reiniciar_tabuleiro()
                jogo.jogador_atual = random.choice([jogador1, jogador2])
                input(f'\nNovo jogo! {jogo.jogador_atual.nome} começa! Pressione Enter...')
                

            elif jogo.tabuleiro_cheio():
                
                jogo.mostrar_tabuleiro()
                print('\nEmpate!\n')
                if input('Jogar novamente? (s/n): ').lower() != 's':
                    break

                jogo.reiniciar_tabuleiro()
                jogo.jogador_atual = random.choice([jogador1, jogador2])
                input(f'\nNovo jogo! {jogo.jogador_atual.nome} começa! Pressione Enter...')
                
            else:
                jogo.trocar_jogador()
        else:
            print('Posição inválida ou já ocupada. Tente novamente.')


if __name__ == '__main__':
    main()
