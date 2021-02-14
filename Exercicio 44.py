from time import sleep
print('Programa que calcula o valor a ser pago por um produto, de acordo com o meio de pagamento')
print('\033[33m='*30)
print('MERCADINHO DO PROGRAMADOR')
print('='*30)
print('\033[m')
print('Digite: 01 - MICROSYSTEM / 02 - TELEVISOR 60P / 03 - MICROONDAS')
op = int(input('CODIGO DO PRODUTO :'))
if op == 1:
    valor = 300
elif op == 2:
    valor = 2100
elif op == 3:
    valor = 450

print('O MICROSYSTEM custa R${} avista'.format(valor))
print('Qual a forma de pagamento? 1 - CARTÃO / 2 - CARTÃO PARCELADO / 3 - AVISTA/CHEQUE')
pg = int(input('Digite a forma de pagamento: '))
if pg == 1:
        print('Insira o cartão...')
        sleep(2)
        print('Pagamento efetual com sucesso no valor de R${} com 5% de desconto'.format(valor))
        print('Você pagou R${} e economizou R${}'.format(valor - (valor * 5 / 100), valor * 5 / 100))
elif pg == 2:
        print('Você deve efetuar o pagamento agora de R${} reais'.format(valor))
        print('Insira o cartão...')
        sleep(2)
        parcelas = int(input('Digite o numero de parcelas de até 12x sem juros:'))
        if parcelas <= 2:
            sleep(1)
            print('Pagamento efetuado com sucesso no valor de R${} reais'.format(valor))
        else:
            print('Pagamento efetuado com sucesso no valor de {} reais, foi adicionado ao valor juros de 20% do parcelamento'.format(
                    valor + (valor * 20 / 100)))
            print('Valor das parcelas: {} vezes de R${} reais '.format(parcelas,(valor + (valor * 20 / 100))/parcelas ))

elif pg == 3:
        print('Parabéns, você ganhou 10% de desconto por comprar avista')
        sleep(2)
        print('Recebendo o valor de R${} reais em dinheiro/cheque AVISTA'.format(valor - (valor * 10 / 100)))
        sleep(2)
        print('Pagamento efetuado com sucesso!')
