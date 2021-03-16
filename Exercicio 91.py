#Programa que sorteia valores e poem em um dicionario em ordem
from random import randint as r
from time import sleep
from operator import itemgetter
jogo = {
    "Jogador 1": r(1, 6),
    "Jogador 2": r(1, 6),
    "Jogador 3": r(1, 6),
    "Jogador 4": r(1, 6)
}
ranking = ()
print('Valores sorteados')
for k, v in jogo.items():
    print(f'{k} jogou {v}')
    sleep(0.2)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('-' * 30)
for k, v in enumerate(ranking):
    print(f'O {v[0]} tirou {v[1]} nos dados')
    sleep(1)