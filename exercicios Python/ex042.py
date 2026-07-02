n1 = float(input('Qual comprimento da primera reta: '))
n2 = float(input('Qual comprimento da segunda reta: '))
n3 = float(input('Qual comprimento da terceira reta: '))

if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    print('Esses segmentos formam triângulos')
    if n1 == n2 == n3:
        print("Esse triângulo é EQUILÁTERO!")
    elif n1 != n2 != n3 != n1:
        print ("Esse triângulo é ESCALENO!")
    else:
        print ('Esse triângulo é ISÓCELES!')
else:
    print('Esses segmentos não formam triângulos')