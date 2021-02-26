#Progressão aritimetica aprimorada!
primeiro = int(input('Primeiro :'))
razao = int(input('Razao :'))
termo = primeiro
cont = 1
adc = 1
while not cont == 10:
    print(termo, end=' ')
    termo = termo + razao
    cont = cont + 1
print('PAUSE')
while not adc == 0:
    adc = int(input('\nDeseja mostrar quantos termos a mais?'))
    cont2 = adc + cont
    while not cont == cont2:
            print('{}'.format(termo), end=' ')
            termo = termo + razao
            cont = cont + 1
    if adc != 0:
        print('PAUSE')
    else:
        print('FIM')


