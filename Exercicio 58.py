#Computador gera numero aleatorio para usuario acertar numero
from random import randint
print('Sou seu computador...\nAcabei de pensar um numero entre 0 e 10\nSerá que você consegue adivinhar qual foi?')
palpite = int(input('Qual o seu palpete? '))
pc = randint(0, 100)
c = 1
while not palpite == pc:
    if palpite < pc:
        print('\033[33mMAIS...\033[m tente denovo!')
        palpite = int(input('Qual o proximo palpite? '))
        c += 1
    else:
        print('\033[33mMENOS...\033[m Tente denovo!')
        palpite = int(input('Qual seu proximo palpite? '))
        c += 1

print('\033[33mACERTOU EM {} TENTATIVAS MISERAVI!\033[m'.format(c))