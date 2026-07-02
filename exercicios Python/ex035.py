n1 = float(input('Qual comprimento da primera reta: '))
n2 = float(input('Qual comprimento da segunda reta: '))
n3 = float(input('Qual comprimento da terceira reta: '))

if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    print('Esses segmentos formam triângulos')
else:
    print('Esses segmentos não formam triângulos')