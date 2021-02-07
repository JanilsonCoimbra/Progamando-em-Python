print('Aqui mostramos quando você gasta em litros de tinta para pintar uma parede')
altura = float(input('Aultura da parede: '))
largura = float(input('Largura da parede: '))
area = altura*largura
print('Você tem uma area de {} metros quadrados'.format(area))
print('Para pintar essa area você irá gastar {} litros de tinta'.format(area/2))
