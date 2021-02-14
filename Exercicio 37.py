print('Programa que converte um numero em bianrio, octal ou hexadecimal')
valor = int(input('Digite um numero :'))
print('[1] converter para BINÁRIO')
print('[2] converter para OCTAL')
print('[3] conerter para HEXADECIMAL')
op = int(input('Digite uma OPÇÃO :'))
if op == 1:
    print('O numero {} em binário é {}'.format(valor, bin(valor)[2:]))
elif op ==2:
    print('O numero {} em OCTAL é {}'.format(valor, oct(valor)[2:]))
elif op ==3:
    print('O numero {} em HEXADECIMAL é {}'.format(valor, hex(valor)[2:]))
else:
    print('OPÇÃO ERRADA!')
