#Programa que mostra lista de produtos tabulados
import webbrowser, time
tot = 0
prod = ('Televisor', 1500, 'Computador', 2000, 'Headset', 200,
        'Ecodot', 350, 'Roteador', 100, 'Video Game', 4000, 'Celular', 2000)
for lista in range(0, len(prod)):
    if lista % 2 == 0:
        print(f'{prod[lista]:.<20}', end='')
    if lista % 2 == 1:
        print(f'R${prod[lista]:>10.2f}')
        tot += prod[lista]
print('-' * 32)
print('{:.<20}'.format('TOTAL GASTO'), end='')
print(f'R${tot:>10.2f}')
time.sleep(2)
webbrowser.open('https://www.instagram.com/janilsoncoimbra/',2)
