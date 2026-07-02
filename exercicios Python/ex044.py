print('{:=^40}'.format(' LOJAS MARCELO '))
valor = float(input('Digite um valor do profuto R$: '))
print ('''Lojas Bahia
[1] à Vista em dinheiro
[2] á vista no cartãp
[3] em até 2x no cartão
[4] 3x ou mais no cartão
Escolha uma opção:''')
opcao = int(input('Qual sua opção?'))
if opcao == 1:
    desconto = valor - valor * 0.1
    print ('O produto que custa {} vai custar {} com 10% de desconto'.format(valor, desconto))
elif opcao == 2:
    desconto = valor - valor * 0.05
    print('O produto que custa {} vai custar {} com 5% de desconto'.format(valor, desconto))
elif opcao == 3:
    desconto = valor - valor /2
    print('O produto que custa {} 2x no cartão sai por duas parcelas de {}'.format(valor, desconto))
elif opcao == 4:
    parcelas = int(input('Quantas parcelas? '))
    desconto = valor + valor * 0.20
    final = desconto / parcelas
    print ('O produto que custa {:.2f} vai custar {:.2f} em {} parcelas de {:.2f} com juros de 20%'.format(valor, desconto, parcelas, final))
else:
    total = valor
    print('Opção inválida! Digite de 1 a 4')
