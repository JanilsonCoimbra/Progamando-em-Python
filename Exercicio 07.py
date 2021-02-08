print('Aqui é calculado as notas do aluno para obter a média ')
nota1 = float(input('Digite a nota da primeira unidade: '))
nota2 = float(input('Digite a nota da segunda unidade: '))
nota3 = float(input('Digite a nota da terceira unidade: '))
nota4 = float(input('Digite a nota da quarta unidade: '))

print('Agora vamos ver qual a média do aluno!')

print('A média foi: {:0.1f}'.format((nota1+nota2+nota3+nota4)/4) )