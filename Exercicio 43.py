print('Programa que ler o peso e altura de uma pessoa e calcula o IMC')
peso = float(input('Peso :'))
altura = float(input('Altura :'))

imc = peso / (altura * altura)

if imc < 18.5:
    print('Você está com IMC de {:.2f} e está \033[33mABAIXO DO PESO\033[m'.format(imc))
elif imc < 25:
    print('O valor do seu IMC é {:.2f}, esse \033[33mVALOR IDEAL\033[m'.format(imc))
elif imc < 30:
    print('O valor do seu IMC é {:.2f} e você está \033[33mACIMA DO PESO\033[m'.format(imc))
elif imc < 40:
    print('O valor do seu IMC é {:.2f} e você está em estado de \033[33mOBESIDADE\033[m'.format(imc))
elif imc > 40:
    print('O valor do seu imc é {:.2f} e você esá em estado de \033[33mOBESIDADE MÓRBIDA\033[m'.format(imc))