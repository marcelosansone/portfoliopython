# Operadores aritméticos
# soma +
# subtração -
# multiplacação *
# divisão /
# ** potência
#// divisão inteira
# % resto da divisão
# == sinal de igualdade


# Ordem de precedência
# 1. ()
# 2. **
# 3. * / // %
# 4. + -

#nome = input('Qual é o seu nome?')
#print('Prazer em te conhecer {:=^20}!'.format(nome))

n1 = int(input('Uṁ valor:'))
n2 = int(input('Outro valor:'))
s = n1+n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print ('A soma é {}, o produto é {} e a divisão é {:3}'.format(s,m,d,e))
print('A Divisão inteira {} e potência {}'.format(di,e))
print('A soma vale {}'.format(n1+n2))

# \n quebra linha
# end=' ' final do print para juntar dois prints que estão separados