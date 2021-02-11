print('Programa que calcula o preço da viagem com base na distancia')
distancia = int(input('Qual a distancia da viagem? '))
if distancia <= 200:
    print('O preço da viagem será de R${}'.format(distancia*0.50))
else:
    print('O preço da viagem será de R${}'.format(distancia*0.45))