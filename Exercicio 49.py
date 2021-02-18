#Tabuada simplificada ultilizando estrutura FOR
num = int(input('Digite um numero para ver sua tabuada :'))
for c in range(1, 11):
    result = num * c
    print('{} x {} = {}'.format(num, c, result))