from random import randint
print('Computador escolhe numero de 0 a 5 e usuario tenta adivinhar')
numero = int(randint(0,5))
print(numero)
print('-=-'*20)
escolha = int(input('Escolha um numero de 0 a 5 para jogar...'))
print('-=-'*20)
if numero == escolha:
    print('PARABÉNS VOCÊ GANHOU O PRÊMIO!')
else:
    print('Poxa, não foi dessa vez')

