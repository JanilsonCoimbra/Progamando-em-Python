#Simulador de caixa eletrônico
while True:
    valor = int(input('Valor a ser sacado :'))
    u = valor % 10 // 1
    d = (valor % 100 // 1) - u
    c = (valor % 1000 // 1) - d - u
    m = (valor % 100000 // 1) - u - d - c
    ced1 = u / 1
    ced10 = 0
    ced50 = 0
    if d >= 50:
        ced50 += 1
        ced10 += (d - 50) / 10
    else:
        ced10 += d / 10
    if c >= 100:
        ced50 += (c / 50)
    if m >= 1000:
        ced50 += (m / 50)

    print(f'{int(ced1)} cedulas de R$1,00 real')
    print(f'{int(ced10)} cedulas de 10,00 reais')
    print(f'{int(ced50)} cedulas de R$50,00 reais')
    print('{:-^35}'.format('DINHEIRO SACADO'))
    sac = str(input('Deseja realizar outro saque? [S/N]')).strip().lower()[0]
    if not sac in 's':
        break
