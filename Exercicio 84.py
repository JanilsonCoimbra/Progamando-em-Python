#Programa que ler nome e peso e analisa dados
pessoas = []
cadastro = []
cont = MaiPeso = MenPeso = 0
while True:
    cadastro.append(str(input('Nome :')))
    cadastro.append(float(input('Peso :')))
    print(f'Nome: {cadastro[0]} | Peso: {cadastro[1]}')
    pessoas.append(cadastro[:])
    if cont == 0 or cadastro[1] > MaiPeso:
        MaiPeso = cadastro[1]
    if cont == 0 or cadastro[1] < MenPeso:
        MenPeso = cadastro[1]
    cadastro.clear()
    cont += 1
    conti = str(input('Continuar? [S/N]'))
    if conti in 'nN':
        break
print(f'Ao todo foram cadastrados {cont} pessoas')
print(f'O maior peso foi {MaiPeso}Kg de ', end='')
for p in pessoas:
    if p[1] == MaiPeso:
        print(f'{p[0]} ', end='')
print()
print(f'O menor peso foi {MenPeso}Kg de ', end='')
for p in pessoas:
    if p[1] == MenPeso:
        print(f'{p[0]} ', end='')