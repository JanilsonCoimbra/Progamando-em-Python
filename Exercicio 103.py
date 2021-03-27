#Função que ler nome de um jogador e seus gols e retorna os dados
def ficha(nome="<desconhecido>", gol=0):
    n = nome or '<desconhecido>'
    g = gol or 0
    print(f'O jogador {n} fez {g} gols')


ficha(str(input('Nome :')), input('Gols :'))