print('Programa que mostra se um numero é par ou ímpa')
numero = int(input('Digite um numero: '))
calc = numero % 2
if calc == 0:
    print('Numero é PAR')
else:
    print('Numero é ÍMPAR')
