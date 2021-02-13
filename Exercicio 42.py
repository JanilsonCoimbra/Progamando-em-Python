print('Mostrar se é possivel formar um triangulo e qual o tipo dele, equilatero, isosceles ou escaleno')
l1 = float(input('Lado 1 :'))
l2 = float(input('Lado 2 :'))
l3 = float(input('Lado 3 :'))

if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:

    if l1 == l2 and l1 == l3 and l3 == l2:
        print('Um triangulo \033[33mEQUILATERO\033[m foi formado')
    elif l1 == l2 or l1 == l3 or l2 == l3:
        print('Um triangulo \033[33mISÓSCELES\033[m foi formado')
    elif l1 != l2 and l1 != l3 and l2 != l3:
        print('Um triangulo \033[33mESCALENO\033[m foi formado')
else:
    print('Não foi possivel formar um triangulo')