#Ler numeros e por em uma Matriz de 3x3
matriz = []
x = []
for X in range(1, 4):
    for Y in range(1, 4):
        print(f'Digite um valor para [{X}, {Y}] ', end='')
        x.append(int(input('Valor :')))
    matriz.append(x[:])
    x.clear()
print('-' * 33)
for c in range(0, 3):
    for cont in range(0, 3):
        print(f'[  {matriz[c][cont]:^5}  ]', end='')
    print()
