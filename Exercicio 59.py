#Programa que ler 2 valores e exibe as opções de somar, multiplicar, dizer o maior, digitar novos numeros e SAIR
v1 = int(input('Valor 1 :'))
v2 = int(input('Valor 2 :'))
opcao = ''
while not opcao == 5:
    opcao = int(input('[ 1 ] somar\n[ 2 ] multiplicar\n[ 3 ] maior\n[ 4 ] novos números\n[ 5 ] sair do programa'))
    if opcao == 1:
        print('A soma entre {} + {} = {}'.format(v1, v2, v1+v2))
    if opcao == 2:
        print('A multiplicacao de {} x {} = {}'.format(v1, v2, v1*v2))
    if opcao == 3:
        if v1 > v2:
            print('Entre {} e {} o maior numero é {}'.format(v1, v2, v1))
        elif v2 > v1:
            print('Entre {} e {} o maior numero é {}'.format(v1, v2, v2))
        else:
            print('Os numeros {} e {} são IGUAIS'.format(v1, v2))
    if opcao == 4:
        v1 = int(input('Valor 1 :'))
        v2 = int(input('Valor 2 :'))
print('\033[33mOBRIGADO, VOLTE SEMPRE!\033[m')