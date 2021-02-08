print('Esse codigo exibe a cotação do dólar')
valor = float(input('Digite um valor em reais: '))
print('R${} reais equivale a ${:0.2f} dólar.'.format(valor, valor/3.27))