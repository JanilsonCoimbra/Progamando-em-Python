print('Programa que ler a velocidade de um carro e aplica multa')
velocidade = int(input('Qual a velocidade do carro? '))

if velocidade > 80:
    print('Você foi multado')
    calcvalor = velocidade - 80
    valor = calcvalor * 7
    print('Valor da multa é de {:.2f}'.format(valor))
else:
    print('Você acabou de passar por um radar')
