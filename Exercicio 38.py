print('Programa que ler 2 valores e diz qual o maior')
v1 = int(input('Valor 01 :'))
v2 = int(input('Valor 02 :'))
if v1 > v2:
    print('Entre {} e {} o maior valor é {}'.format(v1, v2, v1))
elif v1 == v2:
    print('Os numeros são iguais!')
else:
    print('Entre {} e {} o maior valor é {}'.format(v1, v2, v2))