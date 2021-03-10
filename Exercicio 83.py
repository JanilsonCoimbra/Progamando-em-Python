#Programa que testa se uma equação é valida
expressao = []
expressao = str(input('Digite a espressão :'))
valores = []
for v in expressao:
    if v == '(':
       valores.append('(')
    elif v == ')':
       if len(valores) > 0:
           valores.pop()
       else:
           valores.append(')')
if len(valores) == 0:
    print('Expressão valida')
else:
    print('Expresão NÃO valida')




