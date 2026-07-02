casa = float(input('Qual valor da casa R$ '))
salario = float(input('Qual o salário do comprador? '))
anos = int(input('Quantos anos de financiamento? '))

prestacao = casa / (anos * 12)
print ('Para pagar uma casa de R${}'.format(casa))
print ('A prestação será de {}'.format(prestacao))
if prestacao < salario * 0.3:
    print ('Sua prestação não excede 30% do seu salário" Empréstimo \033[34mAPROVADO\033[m')
else:
    print ('O valor da prestação é muito alto" Empréstimo \033[31mNEGADO\033[m')