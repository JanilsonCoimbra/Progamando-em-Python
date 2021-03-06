#Programa que ler 5 numeros e insere em ordem na lista sem usar comando sort
valores = [int()]
for c in range(1,6):
    valor = int(input('Digite um valor :'))
    if c == 0 or valor > valores[-1]:
        valores.append(valor)
        print('Valor adicionado no final da lista')
    elif not valor in valores:
        for pos, v in enumerate(valores):
            if v >= valor:
                valores.insert(pos, valor)
                print(f'O valor {valor} foi adicionado na posição {valores.index(valor)}')
                break
print('-' * 30)
print(valores)
print('-' * 30)

