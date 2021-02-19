#Programa que ler 5 pesos em KG e ver qual é o menor peso e o maior
maior = 0
menor = 0
for c in range(1, 6):
    peso = float(input('Peso da {}º pessoa :'.format(c)))
    if peso > maior:
        maior = peso
    elif peso < menor or menor == 0:
        menor = peso
print('\033[31mMenor peso foi {:.2f}Kg\nE maior peso foi {:.2f}Kg\033[m'.format(menor, maior))
