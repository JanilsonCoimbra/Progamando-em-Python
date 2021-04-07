#Programa que acessa sistema de ajuda em python
from time import sleep
cores = (   '\033[m', #neutro
            '\033[1;7;33m', #Amarelo
            '\033[7;94m', #Azul
            '\033[7;97m' #Branco
            )
def titulo(msg, cor=0):
    print(cores[cor], end='')
    print('~' * (len(msg) + 4))
    print(' ', msg)
    print('~' * (len(msg) + 4))
    print(cores[0], end='')
def ajuda(com):
    help(com)


while True:
    titulo('SISTEMA DE AJUDA HELP', 1)
    com = str(input('Digite um comando: '))
    sleep(1)
    if com.lower() == 'sair':
        titulo('Até logo!', 2)
        break
    else:
        print(cores[3], end='')
        ajuda(com)
