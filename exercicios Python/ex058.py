from random import randint

print('Sou seu computador....')
print('Pensei em um número de 0 a 10')

computador = randint(0, 10)
acertou = False
palpite = 0

while not acertou:
    palpite += 1
    jogador = int(input('Qual o seu palpite: '))

    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais....tente novamente')
        elif jogador > computador:
            print('Menos...tente novamente')

print('Você acertou em {} tentativas!'.format(palpite))
