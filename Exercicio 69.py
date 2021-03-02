#Programa que ler dados de pessoas e mostra no final
conti = ''
maior = 0
menor = 0
homens = 0
while True:
    if conti in 'sS':
        idade = int(input('Qual idade :'))
        if idade > 18:
            maior += 1
        sexo = str(input('Qual sexo :')).lower()
        if not sexo in 'fmFM':
            while not sexo in 'fmFM':
                sexo = str(input('Qual sexo :')).lower()
        if sexo == 'm':
            homens += 1
        if sexo == 'f' and idade < 18:
            menor += 1
        conti = str(input('Quer continuar?'))
    elif conti in 'nN':
        break
    else:
        conti = str(input('Quer continuar?'))
print(f'Temos {maior} pessoas maiores de 18 anos')
print(f'Ao todo temos {homens} homens cadastrados')
print(f'Temos ao todo {menor} mulheres menores de idade')

