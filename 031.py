#JOGO SIMPLES DE PEDRA PAPEL E TESOURA COM O COMPUTADOR.

from random import randint
itens = ('pedra', 'papel', 'tesoura')
maquina = randint(0, 2)
print('Vamos Jogar PEDRA PAPEL E TESOURA')
jogador = int(input('''Escolha a sua jogada:
              [0] PEDRA
              [1] PAPEL
              [2] TESOURA
              '''))
print('-='*15)
print('JOGADOR: {}'.format(itens[jogador]))
print('MÁQUINA: {}'.format(itens[maquina]))
print('-='*15)

if maquina ==0:
    if jogador ==0:
        print('EMPATOU!!!')
    elif jogador ==1:
        print('VOCÊ GANHOU! Papel embrulha pedra.')
    elif jogador ==2:
        print('VOCÊ PERDEU! Tesoura corta papel.')

elif maquina ==1:
    if jogador ==0:
        print('VOCÊ PERDEU! Papel embrulha pedra.')
    elif jogador ==1:
        print('EMPATOU!!!')
    elif jogador ==2:
        print('VOCÊ GANHOU! Tesoura corta papel.')

elif maquina ==2:
    if jogador ==0:
        print('VOCÊ GANHOU! Pedra quebra tesoura.')
    elif jogador ==1:
        print(' VOCÊ PERDEU! Tesoura corta papel.')
    elif jogador ==2:
        print('EMPATOU!!!')

else:
    print('JOGADA INVÁLIDA!')
