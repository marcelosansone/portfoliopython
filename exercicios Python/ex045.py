from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
jogador = int(input('''Qual dua jogada?
[0] Pedra
[1] Papel
[2] Tesoura'''))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
sleep(1)
print('-=' * 20)
print('Opção que o jogador jogou {}'.format(itens[jogador]))
print('Opção que o computador jogou {}'.format(itens[computador]))
print('-=' * 20)
if computador == 0: #PEDRA
    if jogador == 0:
        print('Empate')
    elif jogador == 1:
        print('Voce ganhou')
    elif jogador == 2:
        print('O computador ganhou')
    else:
        print('Jogada Inválida!')

elif computador == 1:
    if jogador == 0:
        print ('Voce ganhou')
    elif jogador == 1:
        print ('Empate')
    elif jogador == 2:
        print('O computador ganhou')
    else:
        print('Jogada Inválida!')

elif computador == 2: #TESOURA
    if jogador == 0:
        print('Computador ganhou')
    elif jogador == 1:
        print('Voce ganhou')
    elif jogador == 2:
        print('Empate')
    else:
        print('Jogada Inválida!')
