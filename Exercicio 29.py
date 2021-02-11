print('Programa que ler a velocidade de um carro e aplica multa')
velocidade = float(input('Qual a velocidade do carro? '))

if velocidade > 80 and velocidade <=85:
    print('-=-' * 20)
    print('Você acabou de passar por um radar')
    print('-=-' * 20)
    print('Você está recebendo uma advertencia pro trafegar acima da velocidade permitida')
    print('Você trafegou a uma velocidade de {}'.format(velocidade))
else:
    if velocidade > 85:
        print('-=-'*20)
        print('Você acabou de passar por um radar')
        print('-=-'*20)
        print('Você foi multado por ultrapassar o limite de 80 km da via')
        calcvalor = velocidade - 80
        valor = calcvalor * 7
        print('Valor da multa é de {:.2f}'.format(valor))
    else:
        print('-=-' * 25)
        print('Acabou de passar um radar, tenha um bom dia e dirija com segurança')
        print('-=-' * 25)