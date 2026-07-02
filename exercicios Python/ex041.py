from datetime import date
ano = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = ano - nasc
print('O atleta tem {} anos'.format(idade))
if idade <= 9:
    print('O atleta é da classe MIRIM!')
elif idade > 9 and idade <= 14:
    print('O atleta é da classe INFANTIL')
elif idade >14 and idade <= 19:
    print('O atleta é da classe JUNIOR!')
elif idade > 19 and idade <= 25:
    print('O atleta é da classe MASTER!')
else:
    print('O atleta é da classe SÊNIOR!')


