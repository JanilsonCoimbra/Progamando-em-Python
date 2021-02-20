#Programa de validação de dados
sexo = str(input('Sexo [M/F]')).strip().lower()[0]
while not sexo in 'mf':
    sexo = str(input('Sexo invalido digite o Sexo correto [M/F]')).strip().lower()[0]
print('O sexo registrado foi {} '.format(sexo.upper()))



