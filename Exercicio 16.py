from math import floor
from time import sleep
print('Programa em python que mostra o numero inteiro de um float')
num = float(input('Digite o valor de entrada: '))
print('O numero inteiro de {} é {}'.format(num, floor(num)))
sleep(10)