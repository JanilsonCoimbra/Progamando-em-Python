#Programa que ler valores e não aceita repetições
valores = []
while True:
    valor = int(input('Digite um valor :'))
    if not valor in valores:
        valores.append(valor)
        print('Valor adicionado com sucesso')
    else:
        print('Valor não adicionado [Valor já existe]')
    cont = str(input('Deseja continuar? [S/N]')).strip().lower()[0]
    if cont != 's':
        break
print('-' * 30)
valores.sort()
print(f'Você digitou os valores {valores}')
