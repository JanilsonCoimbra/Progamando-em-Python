#Some numeros até ser digitado 999 para parar usando While True
cont = 0
n = soma = 0
while True:
    cont += 1
    if n == 999:
        break
    soma += n
    n = int(input(f'Digite num :'))
print(f'A soma dos {cont} numeros é {soma} ')
