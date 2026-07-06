n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
opcao = 0

while opcao != 5:
    print('''    [1] SOMAR
    [2] MULTIPLICAR
    [3] MAIOR
    [4] NOVOS NÚMEROS
    [5] SAIR DO PROGRAMA''')
    opcao = int(input('Selecione uma opção de 1 a 5: '))

    if opcao == 1:
        soma = n1 + n2
        print('A soma de {} + {} é igual a {}.'.format(n1, n2, soma))
    elif opcao == 2:
        prod = n1 * n2
        print('A multiplicação de {} e {} é igual a {}.'.format(n1, n2, prod))
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('Entre {} e {} o maior número é {}'.format(n1, n2, maior))
    elif opcao == 4:
        print('Informe os números novamente')
        n1 = int(input('Digite o primeiro valor: '))
        n2 = int(input('Digite o segundo valor: '))
    elif opcao == 5:
        print('-=' * 20)
        print('Finalizando...')
    else:
        print('Opção inválida! Digite um número de 1 a 5.')
