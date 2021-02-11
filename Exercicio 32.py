from datetime import date
print('Programa que ver se o ano é bixesto')
ano = int(input('Digite um ANO: '))
if ano == 0:
    ano = date.today().year
    print('Estamo no ano de {}'.format(ano))

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é um ano bixesto'.format(ano))
    print(bb)
else:
    print('O ano {} não é um ano bixesto'.format(ano))
