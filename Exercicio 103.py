#Função que ler nome de um jogador e seus gols e retorna os dados
def ficha(nome, gol=0):
    jogador = ''
    gols = 0
    if gol.isnumeric():
        gols = gol
    else:
        gols = 0
    if nome.strip() == '' or nome.isnumeric():
        jogador = 'Desconhecido'
        print('O nome do jogador foi deixado vazio ou numerico ')
    else:
        jogador = nome
    print(f'Nome: {jogador}, Gols: {gols}')


ficha(str(input('Nome :')), input('Gols :'))