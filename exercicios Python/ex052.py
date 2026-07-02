num = int(input('Digite um número:'))
total = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[1;31m', end=' ')
        total += 1
    else:
        print('\033[1;33m', end=' ')
    print('{}'.format(c), end=' ')
print('\035[1;33m \nO número {} foi divisível {} vezes'.format(num, total))
if total == 2:
    print('E por isso ele é primo')
else:
    print('E por isso ele não é primo')