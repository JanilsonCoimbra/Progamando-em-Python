from math import radians, sin, cos, tan
print('Programa que diz o seno, cosseno e tagente do angulo de entrada')
an = float(input('Digite o valor do angulo: '))
radiano = radians(an)
seno = sin(radiano)
cosseno = cos(radiano)
tangente = tan(radiano)
print('O seno do angulo de {} graus é {:.2f}'.format(an, seno))
print('O cosseno do angulo de {} graus é {:.2f}'.format(an,cosseno))
print('A tangente do angulo de {} graus é {:.2f}'.format(an, tangente))
