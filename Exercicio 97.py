#Função que recebe texto e retorna formatado
def escreva(f):
    t = len(f) + 4
    print('~' * t)
    print(f'  {f}')
    print('~' * t)


escreva('Curso em video')
escreva('Gustavo Guanabara')
escreva('CeV')
