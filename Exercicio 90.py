#Programa que ler nome e média de um aluno e guarda a situação dele em um dicionario python
alunos = []
cadastro = dict()
cadastro['Nome'] = str(input('Nome :'))
cadastro['Media'] = int(input(f'Digite a média de {cadastro["Nome"]} :'))
print('-' * 30)
print(f'{"Dados do aluno":^30}')
print('-' * 30)
alunos.append(cadastro.copy())
cadastro.clear()
print(f'Nome : {alunos[0]["Nome"]}')
print(f'Média : {alunos[0]["Media"]}')
if alunos[0]["Media"] < 6:
    alunos[0]["situação"] = 'Reprovado'
    print(f'Situação : {alunos[0]["situação"]}')
else:
    alunos[0]["situação"] = 'Aprovado'
    print(f'Situação : {alunos[0]["situação"]}')

