#Digite um numero até o usuario digitar 999 para parar
n = 0
soma = 0
n = int(input('Digite um numero [999 para parar]'))
while not n == 999:
    soma += n
    n = int(input('Digite um numero [999 para parar]'))
print(soma)