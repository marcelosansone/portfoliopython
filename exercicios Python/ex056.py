somaidade = 0
media = 0
maioridade = 0
nomevelho = ''
totmulher20 = 0
for p in range(1, 5):
    print ('------{} pessoa------'.format(p))
    nome = str(input('Nome:')).strip()
    idade = int(input('Idade:'))
    sexo = str(input('Sexo: [M/F]')).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridade = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridade:
        maioridade = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1
media = somaidade / 4
print ('A média de idade do grupo é de {}'.format(media))
print ('O homem mwiw velho tem {} anos e se chama {}'.format(maioridade, nomevelho))
print('Ao todos são {} mulheres com menos de 20 anos'.format(totmulher20))
