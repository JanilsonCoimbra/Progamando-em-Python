#Programa que recebe 4 numeros e mostra estatisticas
lista = int(input('Digite um numero :')), int(input('Digite um numero :')), int(input('Digite um numero :')), int(input('Digite um numero :'))
print(f'Você digitou os numeros {lista}')
print('-' * 26)
print(f'O numero 9 apareceu {lista.count(9)} vezes')
print(f'o valor 3 apareceu na {lista.index(3) + 1}º posição')
par = 0
for c in range(0, len(lista)):
    if (lista[c] % 2 == 0) == True:
        par += 1
print(f'Foram {par} valores pares digitados')

