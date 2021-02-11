print('Programa que ler 3 numero e ver qual o maior e menor')
n1 = int(input('Primeiro numero :'))
n2 = int(input('Segundo numero :'))
n3 = int(input('Terceiro numero :'))

if n1 > n2 and n1 > n3:
    maior = n1
    print('\nO maior numero é {}'.format(n1))
    if n2 > n3:
        print('\nO menor numero é {}'.format(n3))
    else:
        print('\nO menor numero é {}'.format(n2))

else:
    if n2 > n1 and n2 > n3:
        maior = n2
        print('\nO maior numero é {}'.format(n2))
        if n1 > n3:
            print('\nO menor numero é {}'.format(n3))
        else:
            print('\nO menor numero é {}'.format(n1))
    else:
        if n3 > n1 and n3 > n2:
            maior = n3
            print('\nO maior numero é {}'.format(n3))
            if n1 > n2:
                print('\nO menor numero é {}'.format(n2))
            else:
                print('\nO menor numero é {}'.format(n1))



