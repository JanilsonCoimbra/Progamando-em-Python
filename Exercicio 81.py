#Programa que ler numeros e executa estatistica
valores = []
while True:
    valores.append(int(input('Digite um valor :')))
    contin = str(input('Deseja continuar? [S/N]')).strip().lower()[0]
    if contin == 'n':
        break
print(f'Você digitou {len(valores)} elementos')
b = valores[:]
b.sort(reverse=True)
print(f'Os valores em ordem decrescente são {b}')
if 5 in valores:
    print(f'O valor 5 faz parte da lista e está na posição {valores.index(5)}')
else:
    print('O valor 5 não faz parte da lista!')