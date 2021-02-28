#Digite um numero até o usuario digitar 999 para parar
n = 0
soma = 0
while not n == 999:
    n = int(input('Digite um numero [999 para parar]'))
    if n != 999:
        soma += n
print(soma)