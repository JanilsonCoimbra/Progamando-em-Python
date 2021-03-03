#Simulando Caixa eletronico 2.0
import webbrowser
from time import sleep
while True:
    print('{:-^40}'.format('CAIXA ELETRONICO DO JAPA'))
    cont = 0
    v = int(input('Valor do saque :'))
    while not v == 0:
        cont += 1
        if v < 10:
            nota = 1
            v -= nota
            if v == 0:
                print(f'{cont} Notas de R${nota}')
                cont = 0
        elif v < 20:
            nota = 10
            v -= nota
            if v == 0 or v < 10:
                print(f'{cont} Notas de R${nota}')
                cont = 0
        elif v < 50:
            nota = 20
            v -= nota
            if v == 0 or v < 20:
                print(f'{cont} Notas de R${nota}')
                cont = 0
        elif v >= 50:
            nota = 50
            v -= nota
            if v == 0 or v < 50:
                print(f'{cont} Notas de R${nota}')
                cont = 0
    sleep(1)
    print('Me sigam no instagram para aprendemos PYTHON juntos')
    sleep(2)
    link = "https://www.instagram.com/janilsoncoimbra/"
    webbrowser.open(link,2)
    break



