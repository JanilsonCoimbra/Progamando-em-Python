#função que conta numero de inicio, fim e passo personalizados
from time import sleep
def contagem(*p):
    print('-' * 40)
    print(f'Contagem de {p[0]} até {p[2]} contando de {p[1]} em {p[1]}')
    passo = p[1]
    fim = p[2]
    if p[1] == 0:
        passo = 1
    if p[0] > p[2]:
        passo = p[1] - (p[1] + p[1])
        fim -= 2
    for c in range(p[0], fim+1, passo):
        print(c, end=' ')
        sleep(0.5)
    print()


contagem(0, 2, 10)
contagem(10, 2, 0)
print('-' * 40)
print('Agora é sua vez de personalizar a contagem!')
i = int(input('Inicio :'))
f = int(input('Fim :'))
p = int(input('Passo :'))
contagem(i, p, f)
