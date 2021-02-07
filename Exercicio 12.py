print('Esse programa mostra o preço de um produto e aplica 5% de desconto')
valor = float(input('Qual o valor do produto: '))
print('O valor do produto é {:0.2f} reais e com 5% de desconto fica {:0.2f} reais'.format(valor, valor-(valor*5/100)))