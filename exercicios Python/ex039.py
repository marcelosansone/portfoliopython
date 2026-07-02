from datetime import date
atual = date.today().year
nasc = int(input('Qual o seu ano de nascimento? '))
idade = atual - nasc

if idade < 18:
    print ('Você ainda tem {} anos! Faltam ainda {} anos para seu alistamento'.format(idade, 18-idade))
    ano = atual + idade
    print ('Você deve se alistar no ano {}'.format(ano))
elif idade == 18:
    print ('Você tem 18 anos e deve se alistar imediatamene')
elif idade > 18:
    print ('Você já tem {}, você deveria ter se alistado há {} anos'.format(idade, idade-18))
    ano = atual - idade
    print('Você deveria ter se alistado no ano de {}'.format(ano))
