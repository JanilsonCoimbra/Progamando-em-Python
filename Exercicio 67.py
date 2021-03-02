#Tabuada do numero digitado usando While True
while True:
    n = int(input('Digite um numero :'))
    if n < 0:
        break
    for cont in range(1, 11):
        print(f'{n} x {cont} = {n * cont}')
print('TABUADA ENCERRADA!')
