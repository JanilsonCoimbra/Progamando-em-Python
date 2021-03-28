#Função que só aceita entrada de numeros e trata erros de usuario
def LeiaInt(num):
    print(f'\033[33mVocê digitou o numero {num}\033[m')


while True:
    n = input('Digite um numero ou sair :')
    if n == 'sair':
        break
    if n.isnumeric():
        LeiaInt(int(n))
    else:
        print('\033[94mNÃO É UM NUMERO NUMERICO VALIDO\033[m')

