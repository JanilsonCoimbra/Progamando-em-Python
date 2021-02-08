print('Programa que da um almento de 15% no salario de um funcionário')
salario = float(input('Qual o salario: '))
print('O salário atual é {:0.2f} reais e com um aumento de 15% fica {:0.2f} reais'.format(salario, salario+(salario*15/100)))