print('Programa que mede os lados do triangulo e ver se é possivel formalo')
l1 = float(input('Lado 1 :'))
l2 = float(input('Lado 2 :'))
l3 = float(input('Lado 3 :'))

if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print('Um triangulo foi formado')
else:
    print('Não é possivel formar um triangulo')
