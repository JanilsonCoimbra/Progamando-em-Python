#Tabuada do numero digitado usando While True
while True:
    cont = 0
    n = int(input('Digite um numero :'))
    if n < 0:
        break
    while True:
        print(f'{n} x {cont} = {n * cont}')
        cont +=1
        if cont == 11:
            break
print('TABUADA ENCERRADA!')

