d = float(input('Qual a distância da viagem em km ?'))

if d <= 200:
    valor = d * 0.50
else:
    valor = d * 0.45

print ('{} km serão rodados, portanto a passagem vai custar R${}'.format(d, valor))
