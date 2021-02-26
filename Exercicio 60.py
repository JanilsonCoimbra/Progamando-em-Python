#Exercicio que faz umap rogressão aritimetica
primeiro = int(input('Primeiro termo :'))
razao = int(input('Razão :'))
termo = primeiro
cont = 1
while cont <= 10:
    print(termo, end=' ')
    termo = termo + razao
    cont = cont + 1
print('FIM')


'''for c in range(primeiro, ultimo+razao, razao):
    print('{} ->'.format(c), end=' ')
print('FIM')'''