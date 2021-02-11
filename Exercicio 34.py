print('Programa que ler o salario do funcionario e dar um almento de 15% se ele ganhar menos que 1250')
salario = float(input('Digite qual o seu salario :'))
if salario > 1250:
    salario = salario + (salario * 10 / 100)
    print(salario)
else:
    salario = salario + (salario * 15 / 100)
    print(salario)