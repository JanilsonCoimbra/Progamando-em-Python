#Progressão aritimetica aprimorada!
primeiro = int(input('Primeiro :'))
razao = int(input('Razao :'))
termo = primeiro
cont = 0
adc = 10
total = 0
while not adc == 0:
    total = total + adc
    while not cont == total:
        print('{}'.format(termo), end=' ')
        termo = termo + razao
        cont = cont + 1
    print('PAUSE')
    adc = int(input('\nDeseja mostrar quantos termos a mais?'))
print('FIM')

