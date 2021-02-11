from random import randint
print('Computador escolhe numero de 0 a 99 e usuario tenta adivinhar')
numero = int(randint(0,99))
print(numero)

escolha = int(input('Escolha um numero de 0 a 5 para jogar...'))

if numero == escolha:
    print('PARABÉNS VOCÊ GANHOU O PRÊMIO!')
else:
    print('Poxa, não foi dessa vez')

