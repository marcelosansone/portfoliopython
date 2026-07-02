sal = float(input('Qual o salario do funcionario:'))
aumento = sal * 0.15
final = sal + aumento

print ('O funcionário que recebia R${}, teve um aumento de {} e passará a receber R${:.2f} reais'.format(sal, aumento, final))