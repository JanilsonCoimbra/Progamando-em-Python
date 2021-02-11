from random import choice
print('Programa que escolhe entre 4 alunos 1 para apagar o quadro')
a1 = str(input('Primeiro aluno: '))
a2 = str(input('Segundo aluno: '))
a3 = str(input('Terceiro aluno: '))
a4 = str(input('Quarto aluno: '))
lista = [a1, a2, a3, a4]
escolhido = choice(lista) #Choice escolhe um valor aleatorio de umalista
print('O aluno escolhido foi {}'.format(escolhido))
