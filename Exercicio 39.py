from datetime import date
print('Programa que ler o ano de nascimento de um jovem e ver se ele pode ir alistar-se no exercito')
nasc = int(input('Em que ano você nasceu?'))
ano = date.today().year
if ano - nasc >=18:
    print('Você tem {} anos e já passou {} anos do prazo para alistar-se'.format(ano - nasc,ano - nasc -18 ))
else:
    print('Você tem {} anos e ainda falta {} anos para alistar-se'.format(ano - nasc, 18 - (ano - nasc)))