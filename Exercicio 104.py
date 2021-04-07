#Função que só aceita entrada de numeros e trata erros de usuario
def LeiaInt(msg):
    valor = 0
    while True:
        n = str(input(msg))
        print(f'\033[33mVocê digitou o numero {n}\033[m')
        if n == 'sair':
            break
        if n.isnumeric():
            valor = int(n)
        else:
            print('\033[94mNÃO É UM NUMERO NUMERICO VALIDO\033[m')

LeiaInt('Digite um numero ou sair :')
