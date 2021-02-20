#Programa que ler 2 valores e exibe as opções de somar, multiplicar, dizer o maior, digitar novos numeros e SAIR
v1 = int(input('Valor 1 :'))
v2 = int(input('Valor 2 :'))
opcao = ''
while not opcao == 5:
    opcao = int(input('[ 1 ] somar\n[ 2 ] multiplicar\n[ 3 ] maior\n[ 4 ] novos números\n[ 5 ] sair do programa'))
    if opcao == 1:
        print('\033[33mA soma entre {} + {} = {}\033[m'.format(v1, v2, v1+v2))
    elif opcao == 2:
        print('\033[33mA multiplicacao de {} x {} = {}\033[m'.format(v1, v2, v1*v2))
    elif opcao == 3:
        if v1 > v2:
            print('\033[33mEntre {} e {} o maior numero é {}\033[m'.format(v1, v2, v1))
        elif v2 > v1:
            print('\033[33mEntre {} e {} o maior numero é {}\033[m'.format(v1, v2, v2))
        else:
            print('\033[33mOs numeros {} e {} são IGUAIS\033[m'.format(v1, v2))
    elif opcao == 4:
        v1 = int(input('\033[33mValor 1 :\033[m'))
        v2 = int(input('\033[33mValor 2 :\033[m'))
    elif opcao > 5:
        print('\033[33mOPÇÃO INVALIDA!\033[m')
print('\033[33mOBRIGADO, VOLTE SEMPRE!\033[m')