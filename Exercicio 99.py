#função que analisa valores informados e diz qual o maior e quantos foram
from time import sleep
def maior(*v):
    maior = cont = 0
    print('-=' * 30)
    for c in v:
        print(c, end=' ')
        sleep(0.5)
        cont += 1
        if maior < c:
            maior = c
    print(f'Foram digitados {cont} valores e o\nmaior numero digitado foi o {maior}')
maior(4, 5, 8, 10, 3, 6)
maior(8, 5, 0, 9, 6)
maior(8)