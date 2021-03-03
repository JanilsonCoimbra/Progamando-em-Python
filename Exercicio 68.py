#Jogo de PAR ou IMPAR, usuario VS PC
from random import randint
from time import sleep
ganhou = perdeu = 0
while True:
    pc = randint(0, 10)
    sleep(1)
    v = int(input('Diga um valor :'))
    pi = str(input('Par ou Ímpar? [P/I]')).strip().lower()[0]
    if not pi in 'piPI':
        while True:
            pi = str(input('Par ou Ímpar? [P/I]')).strip().lower()[0]
            if pi in 'PIpi':
                break
    r = (pc + v) % 2
    if pi in 'pP':
        a = 0
    elif pi in 'iI':
        a = 1
    print('-=-' * 18)
    print(f'Você jogou {v} e o PC jogou {pc} no total deu {v + pc} que é {"PAR" if r == 0 else "ÍMPAR"}')
    print('-=-' * 18)
    if a == r:
        sleep(1)
        print('\033[33mVOCÊ GANHOU\033[m')
        ganhou += 1
    else:
        sleep(1)
        print('\033[33mPC GANHOU\033[m')
        perdeu += 1
        break
sleep(1)
print(f'GAME OVER \nVocê ganhou {ganhou} e perdeu {perdeu} vez')



