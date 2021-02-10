print('Programa que ler o nome completo de uma pessoa e manipule com funções de texto')

nome = str(input('Qual o seu nome? '))
nome = nome.strip() #remove espaços das estremidades

print('Seu nome em maiusculo usando upper() ', nome.upper()) #letras maiusculas
print('Seu nome em minusculo usando lower() ', nome.lower()) #letras minusculas
print('Seu nome ultilizando comando capitalize()', nome.capitalize()) #primeira letra da frase maiuscula

separado = nome.split() #separando os nomes em lista
espaco = len(separado)-1 #contando quantas palavras tem na lista
print('Numero de letras do primeiro nome com o comando len(separado[0]',len(separado[0])) #quantas letras tem na primeira palavra da lista
print('Numero de espaços feito com comando len(separado)-1 no nome é ',espaco)


