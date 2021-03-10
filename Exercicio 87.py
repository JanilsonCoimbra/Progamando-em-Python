#Programa que ler numeros, poem em uma matriz 3x3 e depois analisa os dados
matriz = []
numeros = []
for c in range(1, 4):
    for c1 in range(1, 4):
        print(f'Digite o valor [{c}, {c1}] :')
        numeros.append(int(input('Valor :')))
    matriz.append(numeros[:])
    numeros.clear()
contPar = SomaPar = Soma3Col = MaioValCol3 = 0
for cont in range(0, 3):
    for cont1 in range(0, 3):
        print(f'[  {matriz[cont][cont1]}  ]', end='')
        if matriz[cont][cont1] % 2 == 0:
            contPar += 1
            SomaPar += (matriz[cont][cont1])
        if matriz[cont][cont1] == matriz[cont][2]:
            Soma3Col += matriz[cont][cont1]
        if matriz[cont][cont1] == matriz[1][cont1]:
            if matriz[1][cont1] > MaioValCol3:
                MaioValCol3 = matriz[cont][cont1]
    print()
print(f'Os numeros pares são {contPar} que somados dão {SomaPar}')
print(f'A soma dos valores da terceira coluna da {Soma3Col}')
print(f'O maior valor da linha 3 é {MaioValCol3}')