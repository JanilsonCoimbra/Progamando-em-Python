from datetime import date
print('Programa que ler o ano de nascimento de um jovem e ver se ele pode ir alistar-se no exercito')
nasc = int(input('Em que ano você nasceu?'))
ano = date.today().year
if ano - nasc >18:
    saldo = ano - nasc -18
    print('Você tem {} anos e já passou {} anos do prazo para alistar-se'.format(ano - nasc,saldo ))
    alist = ano - saldo
    print('Seu alistamento foi em {}'.format(alist))
elif ano - nasc == 18:
    print('Você deve alistar-se IMEDIATAMENTE')
else:
    saldo = 18 - (ano - nasc)
    print('Você tem {} anos e ainda falta {} anos para alistar-se'.format(ano - nasc, 18 - (ano - nasc)))
    alist = ano + saldo
    print('Seu alistamento vai ser em {}'.format(alist))