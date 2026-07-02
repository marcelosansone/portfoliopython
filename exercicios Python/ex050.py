s = 0
count = 0
for c in range(1, 7):
    n = int(input('Digite um {} número:'.format(c)))
    if n % 2 == 0:
        s += n
        count += 1
print('A soma dos {} números pares digitados foi {}'.format(count, s))