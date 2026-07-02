km = float(input('Qual a quantidade de km percorrido: '))
dia = int(input('Qual a quantidade de dias alugado: '))

fdia = dia * 60
fkm = km * 0.15
final = fdia + fkm

print ('A quantidade de km rodados foi de {:.2f} km e por {:.1f} dias.\nPortanto o valor final'
       'do aluguel do caro será de R$ {}'.format(km, dia, final))