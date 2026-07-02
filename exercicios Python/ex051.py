primeiro = int(input('Primeiro termo: '))
razao = int(input('Qual a razao: '))
decimo = primeiro + (10 - 1) * razao
for c in range(primeiro, decimo + razao, razao):
    print(c, end=' ')
print('FIM')

