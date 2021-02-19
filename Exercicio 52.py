#Programa que ver se o numero é numero primo ou não
n = int(input('Digite um numero :'))
cont = 0
for c in range(1, n+1):
    if n % c == 0:
        cont += 1
        print('\033[33m{}\033[m'.format(c), end=' ')
    else:
        print('\033[31m{}\033[m'.format(c), end=' ')
if cont > 2:
    print('\nO numero {} foi divisivel {} vezes\nE por isso {} não é numero PRIMO'.format(n, cont, n))
else:
    print('\nO numero {} foi divisivel {} vezes\nE por isso {} é numero PRIMO'.format(n, cont, n))
