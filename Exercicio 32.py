print('Programa que ver se o ano é bixesto')
ano = int(input('Digite um ANO: '))
b = ano % 4
bb = ano % 100
if b == 0 and bb != 0:
    print('O ano {} é um ano bixesto'.format(ano))
    print(bb)
else:
    print('O ano {} não é um ano bixesto'.format(ano))