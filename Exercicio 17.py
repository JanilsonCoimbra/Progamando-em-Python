from time import sleep
from math import hypot
print('Programa que ler o comprimento do cateto oposto e \nadjacente de um triangulo e mostra o valor da hipotenusa')
sleep(2)
print('{}'.format('='*100))
cto = float(input('Valor do cateto oposto do triangulo: '))
cta = float(input('Valor do cateto adjacente do triangulo: '))

print('O valor da hipotenusa é {:0.2f}'.format(hypot(cto, cta)))

