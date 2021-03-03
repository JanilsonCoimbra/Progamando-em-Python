#Programa que ler nome e valor de produtos e mostra estatistica
print('-' * 16)
print('MERCADO DO JAPA')
print('-' * 16)
ProdMenorValor = ''
totcom = MaisMil = MenorValor = 0
while True:
    produto = str(input('Produto :'))
    valor = float(input('Valor :'))
    if valor > 1000:
        MaisMil += 1
    if totcom == 0 or valor < MenorValor:
        ProdMenorValor = produto
        MenorValor = valor
    totcom += valor
    fim = str(input('Cadastrar Novo Produto? [S/N]')).strip().lower()[0]
    if fim in 'n':
        break
print('{:-^40}'.format('FIM DO PROGRAMA'))
print(f'O total da compra foi de R${totcom:.2f}')
print(f'Temos {MaisMil} produto custando acima de R$1000.00')
print(f'O produto mais barato foi {ProdMenorValor} custando {MenorValor:.2f}')
