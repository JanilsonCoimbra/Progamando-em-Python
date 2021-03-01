#Programa que mostra media e diz maior e menor valor
n = 0
continua = 's'
soma = cont = media = maior = menor = 0
while continua in 'Ss':
    n = int(input('Digite um numero :'))
    soma += n
    cont += 1
    if cont == 1:
        maior = menor = n
    elif n > maior:
        maior = n
    elif n < menor:
        menor = n
    continua = str(input('Deseja continuar? [S/N]')).lower().strip()[0]
media = soma/cont
print('A soma de todos os {} numeros é {} e a média é {:.2f}'.format(cont, soma, media))
print('Menor valor é {} e maior valor é {}'.format(menor, maior))