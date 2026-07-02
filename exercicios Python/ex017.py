from math import hypot
co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))
hyp = hypot(co, ca)
print ('O triangulo com cateto oposto de {} e catetoadjacente {} tem uma hipotenusa de {:.2f}'.format(co, ca, hyp))