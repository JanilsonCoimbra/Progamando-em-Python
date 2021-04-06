#Função que ler nome de um jogador e seus gols e retorna os dados
def ficha(nome='<desconhecido>', gol=0):
    n = nome
    g = gol
    if g.isnumeric():
        g = int(g)
    else:
        g = 0
    if n.strip() == '':
        ficha(gol=g)
    else:
        ficha(n, g)
    print(f'O jogador {nome} fez {g} gols')


ficha(str(input('Nome :')), input('Gols :'))