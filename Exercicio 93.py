#Programa que analisa um jogador de futebol
cadastro = dict()
nome = str(input('Nome do jogador :'))
cadastro["nome"] = nome
c = int(input(f'Quantas partidas {nome} jogou? '))
gols = []
totGols = 0
for cont in range(1, c+1):
    gol = int(input(f'Quantos Gols na {cont} partida?'))
    gols.append(gol)
    totGols += gol
print('-=' * 25)
cadastro["gols"] = gols.copy()
cadastro["total"] = totGols
print(cadastro)
print('-=' * 25)
for k, v in cadastro.items():
    print(f'O campo {k} tem o valor {v}')
print('-=' * 25)
print(f'O jogador {cadastro["nome"]} jogou {cont} partidas.')
for v in range(0, cont):
    print(f'    => O jogador fez na {v+1}º partida {cadastro["gols"][v]} gols')
