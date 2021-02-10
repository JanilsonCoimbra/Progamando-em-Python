print('Programa que ler um numero e diz quantas milhar, centenas, dezenas e unidades existem')
numero = int(input('Digite o numero que deseja: '))
u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10
print('O numero {} tem {} unidades'.format(numero, u))
print('O numeor {} tem {} dezenas'.format(numero, d))
print('O numeor {} tem {} centenas'.format(numero, c))
print('O numeor {} tem {} Milhares'.format(numero, m))


