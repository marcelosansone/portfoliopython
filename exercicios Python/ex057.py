sexo = str(input('Digite o sexo [M/F] ')).upper().strip()[0]
while sexo not in 'MF':
    sexo = str(input('Dados inválidos! Digite o sexo [M/F] ')).upper().strip()[0]
print ("Você digitou o sexo {}".format(sexo))