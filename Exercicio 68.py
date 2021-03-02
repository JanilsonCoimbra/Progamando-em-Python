#Jogo de PAR ou IMPAR, usuario VS PC
from random import choice, randint
from time import sleep
pc = ''
numero = 0
vitorias = 0
derrotas = 0
while True:
    valor = randint(0, 10)
    escolha = int(input('Digite [1] para escolher ÍMPAR ou [0] para PAR :'))
    if escolha == 1:
        sleep(1)
        print(f'\033[33mVocê escolheu ÍMPAR\033[m')
    elif escolha == 0:
        print('\033[33mVocê escollheu PAR\033[m')
    numero = int(input('Digite um numero :'))
    res = (valor + numero) % 2
    if res == escolha:
        print(f'\033[33mO PC escolheu {valor} e você {numero}\033[m')
        sleep(1)
        print('PARABÉNS, VOCÊ GANHOU!')
        vitorias += 1
    else:
        print(f'\033[33mO PC escolheu {valor} e você {numero}\033[m')
        sleep(1)
        print('AHAHHA EU GANHEI!')
        derrotas += 1
        break
print(f'Você Ganhou\033[33m {vitorias} \033[m e perdeu \033[33m {derrotas}\033[m')