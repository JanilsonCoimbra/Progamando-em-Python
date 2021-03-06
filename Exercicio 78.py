#Programa que ler valores e diz qual maior e menor e suas posições na lista
valor = list()
for cont in range(0, 3):
    valor.append(int(input('Digite os valores :')))
if valor.count(min(valor)) > 0:
    print(f'O menor valor foi {min(valor)} nas posições ', end='')
    for pos, valores in enumerate(valor):
        if valores == min(valor):
            print(f'...{pos}', end='')
    print('')
else:
    print(f'O menor valor digitado foi {min(valor)} na posição {valor.index(min(valor))}')
if valor.count(max(valor)) > 1:
    print(f'O maior valor digitado foi {max(valor)} nas posições ',end='')
    for pos, valores in enumerate(valor):
        if valores == max(valor):
            print(f'  ...{pos}',end='')
    print('')
else:
    print(f'O maior valor digitado foi {max(valor)} na posição {valor.index(max(valor))}')
    print('')
