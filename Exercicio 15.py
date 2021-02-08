from time import sleep
print('Total a pagar por um Aluguel de um carro com base na diaria e kilometragem')
dias = int(input('Quantos dias permaneceu com o carro? '))
km = float(input('Quantos kilometros rodados durante a locação? '))
pago = (60*dias) + (km*0.15)
print('Total a pagar pela locação do carro é de R${:0.2f}'.format(pago))
sleep(10)