#Tabuada simplificada ultilizando estrutura FOR
num = int(input('Digite um numero para ver sua tabuada :'))
for c in range(1, 11):
    print('{} x {} = {}'.format(num, c, num * c))