altura = float(input('Qual a sua altura em metros? '))
peso = float(input('Qual o seu peso em Kg? '))
imc = peso / (altura ** 2)

print('O sua altura é {} m, seu peso {} kg e seu IMC {:.1f}'.format(altura, peso, imc))
if imc < 18.5:
    print ('O seu peso está abaixo do ideal')
elif imc >= 18.5 and imc <= 25:
    print ('Seu pedo está na faixa ideal!')
elif imc > 25 and imc <= 30:
    print('Você está com sobrepeso!')
elif imc > 30 and imc <= 40:
    print('Você está com obesidade!')
else:
    print ('Você está com obesidade mórbida!')