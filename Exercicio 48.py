print('Soma de todos os numeros multiplos de 3 de 1 até 500')
soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        soma += c
        cont += 1
print('Foram solicitados {} numeros, que somaram num total {}'.format(cont, soma))
