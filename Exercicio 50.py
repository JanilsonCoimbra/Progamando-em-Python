#Programa que soma os valores digitados e mostra o resultado
soma = 0
cont = 0
for c in range(1, 7):
    num = int(input('Digite o {}º valor :'.format(c)))
    if num % 2 == 0:
        soma += num
        cont += 1
print('Foram somados {} numeros que deram {} somados '.format(cont, soma))
