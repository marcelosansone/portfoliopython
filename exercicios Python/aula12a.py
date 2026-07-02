nome = str(input('Qual o seu nome ?'))
if nome == 'Gustavo':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo' or nome =='Ana':
    print('Seu nome é bem popular no Brasil')
elif nome in 'Carlos Marcelo Luis Bianca':
    print ('Gosto muito desse nome!')
else:
    print ('Tenha um bom dia {}'.format(nome))
print ('Até logo, {}!'.format(nome))
