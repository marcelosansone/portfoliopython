salario = float(input('Digite o seu salario: '))

if salario <= 1250:
    final = salario +(salario * 0.1)
else:
    final = salario +(salario * 0.15)

print('O funcionário que ganhava R$ {:.2f}, recebeu um aumento e passará a ganhar R$ {:.2f}'.format(salario, final))

