#Programa que ler 7 anos, pega a idade e ver quais são maiores e menores de 18 anos
from datetime import date
maior = 0
menor = 0
atual = date.today().year
for c in range(1 , 8):
    ano = int(input('Ano de nascimento :'))
    idade = atual - ano
    if idade >= 18:
        maior += 1
    else:
        menor += 1
print('Tivemos {} pessoas maior de idade\nE {} pessoas menor de idade'.format(maior, menor))
