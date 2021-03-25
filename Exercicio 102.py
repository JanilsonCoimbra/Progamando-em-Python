def fatorial(valor, show=False):
    """
    #Função que retorna o fatorial de um numero inteiro se parametro show=True ela diz como fez o calculo
    :param valor: Numero para calcular o fatorial
    :param show: Parametro que retorna o calculo
    :return: Retorna fatorial de numero
    """
    f=1
    for c in range(valor, 0, -1):
        f *= c
        if show == True:
            if c != valor:
                print('x', end=' ')
            print(f'{c}', end=' ')
            if c == 1:
                print(f'= {f}')
    if show == False:
        print(f)
fatorial(5, show= True)
help(fatorial)