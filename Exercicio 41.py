from datetime import date
print('Programa que diz a categoria de um aluno de natação de acordo com idade')
ano = date.today().year
nasc = int(input('Digite em que ano você nasceu :'))
idade = ano - nasc
if idade <=9:
    print('Atleta MIRIM')
elif idade <= 14:
    print('Atleta INFANTIL')
elif idade <= 19:
    print('Atleta JUNIOR')
elif idade <= 20:
    print('Atleta SÊNIOR')
elif idade > 60:
    print('Atleta APOSENTADO')
else:
    print('Atleta MASTER')
