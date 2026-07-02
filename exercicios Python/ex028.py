import random
from time import sleep
n =random.randint(0,5) #randomiza um número de 0 a 5
num = int(input('Em qual número eu pensei? ')) #jogador tenta adivinhar
print ('Processando...aguarde...')
sleep(2)
if n == num:
    print('Parabéns, o número escolhido foi {}'.format(num))
else:
    print('Você perdeu!Eu pensei no núemro {} e não no número {}'.format(n,num))