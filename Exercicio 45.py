from random import choice
print('Programa que joga pedra, papel e tesoura')
v1 = str('Pedra')
v2 = str('Papel')
v3 = str('tesoura')
opcoes = [v1, v2, v3]
pc = choice(opcoes).lower()
eu = str(input('Escolha pedra, pepel ou tesoura :')).lower()
if pc == eu:
    print('O JOGO EMPATOU')
elif pc == 'pedra' and eu == 'tesoura' or pc == 'tesoura' and eu == 'papel' or pc == 'papel' and eu == 'pedra':
    print('O COMPUTADOR ESCOLHEU {} E GANHOU DE VOCÊ'.format(pc).upper())
else:
    print('VOCÊ VENCEU, PARABÉNS')
    print('COMPUTADOR = {}'.format(pc).upper())

