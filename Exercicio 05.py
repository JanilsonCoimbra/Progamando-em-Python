print('VAmos ler um numero e mostrar seu sucessor e antercessor')
valor = int(input('Agora para iniciar digite o numero: '))
print('O antercessor de {} é {}'.format(valor, valor - 1), end='')
print(', Agora o sucessor é {}'.format(valor + 1))
