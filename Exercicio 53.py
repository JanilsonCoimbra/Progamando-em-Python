#Programa que ver se nome ou frase é palindromo
frase = str(input('Digite a frase :')).strip().upper()
separado = frase.split()
junto = ''.join(separado)
contrario = junto[::-1]
if junto == contrario:
    print('é palindromo')
else:
    print('Não é palindromo')