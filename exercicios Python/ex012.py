preco = float(input('Qual o valor do preço do produto: '))
desc = preco * 0.05
final = preco - desc

print('O preço {:.2f} com 5% de desconto sai por R${:.2f}'.format(preco, final))
