#programa que vende rifa de dezena
dezena = []
nome = []
c = 0
r = -1
while not r == 'n' or c == 100:
    print('[{}] = Numeros vendidos'.format(c))
    r = str(input('Deseja realizar outra venda? [S/N] ')).lower()
    if r == 's':
        n = str(input('Nome :'))
        dez = int(input('Dezena :'))
        if dez > 99:
            print('Escolha de 00 a 99')
            dez = int(input('Dezena :'))
        if dez in dezena:
            print('Dezena vendida, escolha outra!')
        else:
            nome += [n]
            dezena += [dez]
            c += 1
for o in range(0, c):
    print('[{}] :'.format(dezena[o]), end=' ')
    print(nome[o].upper())



