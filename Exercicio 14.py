from time import sleep
print('Programa que convert uma temperatura em Cº para ºF')
sleep(2)
c = float(input('Digite qual a temperatura em C°: '))
f= ((9*c)/5)+32
print('A temperatura de {} C° equivale a {} F° '.format(c, f))
sleep(10)