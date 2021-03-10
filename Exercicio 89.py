#Cadastro de alunos com 2 notas e analise no final
alunos = []
estudante = []
notas = []
while True:
    estudante.append(str(input('Nome do aluno :')))
    for c in range(1, 3):
        notas.append(float(input(f'Nota {c} :')))
    estudante.append((notas[0] + notas[1]) / 2)
    estudante.append(notas[:])
    notas.clear()
    alunos.append(estudante[:])
    estudante.clear()
    conti = str(input('Deseja continuar? [S/N]')).strip().lower()[0]
    if conti in 'nN':
        break
print(f'{"No":<4} {"NOME":<10}{"MÉDIA":>8}')
print('-' * 23)
for no, a in enumerate(alunos):
    print(f'{no:<4} {a[0]:<10} {a[1]:>5}')
while True:
    NotaAluno = int(input('Mostrar nota de qual aluno? '))
    if NotaAluno == 999:
        break
    print('-' * 30)
    print(f'A nota de {alunos[NotaAluno][0]} é {alunos[NotaAluno][2]}')
    print('-' * 30)
