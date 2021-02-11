from math import trunc
from time import sleep
print('Programa em python que mostra o numero inteiro de um float')
num = float(input('Digite o valor de entrada: '))
print('O numero inteiro de {} é {}'.format(num, trunc(num))) # trunc exibe o valor inteiro do numero
sleep(10)
