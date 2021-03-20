#Programa que tem 2 funções, 1 sorteia 5 valores outra soma os valores pares
from random import randint
def sorteio():
    valores = [randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9)]
    return valores
def somaPar(lista):
    soma = cont = contPar = 0
    for v in lista:
        if v%2 == 0:
            contPar += 1
            soma += v
        cont += 1
    print(f'Olhamos os {cont} valores digitados e somamos os {contPar} pares {lista} que deu {soma}')
v = sorteio()
print(f'Sorteando 5 valores da lista {v} PRONTO!')
somaPar(v)
