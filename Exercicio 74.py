#Programa que sorteia 5 numeros e diz qual o maior e menor
from random import randint
lista = (randint(1,9), randint(1,9), randint(1,9), randint(1,9), randint(1,9))
print(lista)
print(f'O menor numero é {sorted(lista)[0]}')
print(f'O maior numero é o {sorted(lista)[-1]}')
