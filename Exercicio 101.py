#Função que retorna com base no ano de nascimento se pode votar
def voto(nasc):
    from datetime import date
    ano = date.today().year
    idade = ano - nasc
    if idade < 16:
        print(f'Com {idade} anos: Não é possovél VOTAR ainda!')
    elif 16 <= idade < 18:
        print(f'Com {idade} anos: O VOTO é opcional ')
    elif idade < 65:
        print(f'Com {idade} anos: VOTO é obrigatório!')
    elif idade > 65:
        print(f' Com {idade} anos: O VOTO é opcional')
while True:
    voto(int(input('Em que ano você nascel?')))
    r = str(input('Continuar? [S/N]')).strip()[0]
    if r in 'nN':
        break
    elif r not in 'nNsS':
        print('Opção invalida!')
