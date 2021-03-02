#Some numeros até ser digitado 999 para parar usando While True
cont = 0
n = soma = 0
while True:
    n = int(input(f'Digite num :'))
    if n != 999:
        soma += n
        cont += 1
    else:
        break
print(f'A soma dos {cont} numeros é {soma} ')
