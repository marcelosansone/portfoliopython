num = int(input('Escolha um número inteiro: '))
print('''Escolha uma das opções:
    [1] Binário
    [2] Octal
    [3] Hexadecimal''')
opcao = int(input('Sua opção: '))
if opcao == 1:
    print('O número {} convertido para binário é {}'.format(num, bin(num)[2:]))
elif opcao == 2:
    print('O núemro {} convertido para octal é {}'.format(num, oct(num)[2:]))
elif opcao == 3:
    print('O número {} convertido para hexadecimeal é {}'.format(num, hex(num)[2:]))
else:
    print ('Opção inválida!')