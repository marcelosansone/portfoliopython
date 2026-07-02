s = 0
count = 0
for c in range(1, 501, 2): #verifica os números ímpares
    if c % 3 == 0:
        count += 1 #conta o número de multiplos de 3
        s += c #soma os númerosímpares divisiveis por 3
        print(c, end=' ')
print ('')
print ('A soma dos números é {}'.format(s))
print('Foram utilizados {} números'.format(count))