#Programa que encontra as vogais em palavras
lista = ('Vento', 'Cadeira', 'Mesa', 'Simpó', 'Curso', 'Programaçao', 'Python')
vog = 'aeiou'
for c in lista:
    print(f'Na palavra {c.upper():.<15}', end='')
    print(f'Temos as vogais (', end='')
    for cont in range(0, (len(c))):
        if c[cont].lower() in vog:
            print(f'{c[cont]}', end='')
    print(')')
