#Levantamento de um jogador de futebol por partida
cadastro = list()
gols = list()
jogador = dict()
cont = 0
while True:
    cont += 1
    print('-=' * 20)
    nome = str(input('Nome do jogador :'))
    jogador["nome"] = nome
    partidas = int(input(f'Quanats partidas {nome} jogou? '))
    jogador["partidas"] = partidas
    for c in range(1, partidas+1):
        gols.append(int(input(f'Quantos gols na {c}º partidas :')))
    jogador["gols"] = gols[:]
    cadastro.append(jogador.copy())
    print(f'\033[33mNome : {jogador["nome"]} | Partidas: {jogador["partidas"]}\033[m')
    jogador.clear()
    gols.clear()
    resposta = str(input('Deseja continuar? [S/N]')).strip().lower()[0]
    if resposta == 'n':
        break
print('-' * 40)
print(f'{"Cod":<5}{"Nome":<15}{"Gols":<15}{"Total":>5}')
print('-' * 40)
somaGols = 0
for c in range(0, cont):
    print(f'{c:<5}{cadastro[c]["nome"]:<15}{cadastro[c]["gols"]}{sum(cadastro[c]["gols"]):>10}')
while True:
    while True:
        dados = int(input('Mostrar dados de qual jogador? '))
        if dados < cont:
            break
        print('\033[33mNÃO TEMOS ESSE JOGADOR CADASTRADO\033[m')
    if dados == 999:
        break
    print(f'\033[33m=> LEVANTAMENTO DO JOGADOR (Nome: {cadastro[dados]["nome"]} | Partidas: {cadastro[dados]["partidas"]})\033[m')
    for p in range(cadastro[dados]["partidas"]):
        print(f'Na partida {p+1} fez {cadastro[dados]["gols"][p]} gols')
