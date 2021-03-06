#Programa que ler varios numeros e separam em 2 listas de pares e impares
from random import randint
lista = [randint(0,9), randint(0,9), randint(0,9), randint(0,9), randint(0,9), randint(0,9), randint(0,9)]
pares = []
impares = []
print(f'Lista completa {lista}')
for v in lista:
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        impares.append(v)
print(f'Numeros pares {pares}')
print(f'Numeros impares {impares}')
