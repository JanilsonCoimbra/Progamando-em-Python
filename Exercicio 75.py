#Programa que recebe 4 numeros e mostra estatisticas
import webbrowser
from time import sleep
lista = int(input('Digite um numero :')), int(input('Digite um numero :')), int(input('Digite um numero :')), int(input('Digite um numero :'))
print(f'Você digitou os numeros {lista}')
print('-' * 26)
print(f'O numero 9 apareceu {lista.count(9)} vezes')
print('O valor 3 apareceu em posição {}'.format(lista.index(3) + 1 if lista.count(3) > 0 else "Nenhuma"))
par = 0
for c in range(0, len(lista)):
    if (lista[c] % 2 == 0) == True:
        par += 1
print(f'Foram {par} valores pares digitados')
sleep(2)
webbrowser.open('https://www.instagram.com/janilsoncoimbra/', 2)
