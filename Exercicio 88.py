#Programa que sorteia numeros da mega sena
from random import randint
from time import sleep
jogos = []
palpites = []
n = int(input('Quantos jogos devem ser gerados ?'))
for cont in range(1, n+1):
    for cont1 in range(1, 7):
        while True:
            dezena = randint(1, 61)
            if not dezena in palpites:
                palpites.append(dezena)
                break
    sleep(1)
    palpites.sort()
    print(f'{cont}º Jogo : {palpites}')
    jogos.append(palpites[:])
    palpites.clear()
