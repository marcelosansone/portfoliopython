resp = 'S'
soma = 0
quant = 0
maior = 0
menor = 0
while resp == 'S':
    num = int(input('Digite um número: '))
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
                maior = num
        if num < menor:
            menor = num


    resp = input('Quer continuar? [S/N] ').strip().upper()

media = soma / quant

print('Você digitou {} números e a média foi {:.2f}'.format(quant, media))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))
