#Programa que ler dados de pessoas e ver a media do grupo, o homem mais velho e mulher menor de 20 anos
maisvelho = ' '
media = 0
velho = 0
mulheres = 0
cont = 0
for c in range(1,5):
    cont += 1
    print('----- {}º PESSOA -----'.format(c))
    nome = str(input('Nome :'))
    idade = int(input('Idade :'))
    sexo = str(input('Sexo [M/F] :')).lower()
    media = media + idade
    if velho < idade and sexo == 'm':
        velho = idade
        maisvelho = nome
    if sexo == 'f' and idade < 20:
        mulheres += 1
print('A media do grupo é de {:.2f} anos'.format(media/cont))
if maisvelho == '' and velho == 0:
    print('Não temos HOMENS nesse grupo')
else:
    print('O homem mais velho é {} e tem {} anos'.format(maisvelho, velho))

if mulheres > 0:
    print('Ao todo são {} mulheres com menos de 20 anos'.format(mulheres))
else:
    print('Não temos Mulheres menores de 20 anos')
