#Função realiza calculo da area
def area(l, c):
    a = l * c
    return a

print('CONTROLE DE TERRENO')
print('-' * 19)
l = float(input('Largura (m) :'))
c = float(input('Comprimento :'))
print(f'A area do terreno de {l} x {c} é de {area(l, c)} metros')
