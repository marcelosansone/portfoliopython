maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input('Digite o peso da {} pessoa: '.format(p)))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
            pessoa = p
        if peso < menor:
            menor = peso
            pessoa = p
print('A pessoa com maior peso com {} kg'.format(maior))
print('A pessoa com menor peso com {} kg'.format(menor))


