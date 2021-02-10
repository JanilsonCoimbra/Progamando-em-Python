print('Programa que ler uma frase e ver se inicia com "santo" diferenciando maiusculas e minusculas')
frase = str(input('Digite a frase aqui: ')).lower().split()
print('santo' in frase[0])