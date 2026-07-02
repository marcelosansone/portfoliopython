frase = str(input('Digite uma frase: ')).strip().upper() #tira espaços vazios a dir e esq e coloca em maiuscula
palavras = frase.split() # tira os espaços
junto = ''.join(palavras) #junta sem espaço
inverso = ''
for letra in range(len(junto)-1, -1, -1):
    inverso += junto[letra]
print(junto, inverso)
if inverso == junto:
    print('Temos um palíndromo')
else:
    print('Essa frase não é um palindromo')rom