#Programa que ler nome, idade e sexo e analisa dados
cadastrados = list()
pessoa = dict()
cont = media = 0
while True:
    pessoa["nome"] = str(input('Nome :'))
    pessoa["sexo"] = str(input('Sexo :'))
    pessoa["idade"] = int(input('Idade :'))
    cadastrados.append(pessoa.copy())
    resposta = str(input('Deseja continuar? [S/N]')).strip(). lower()[0]
    cont += 1
    if resposta == 'n':
        break
print(f'\033[33mForam um total de {cont} pessoas cadastradas.\033[m')
print(f'\033[33mCadastros do sexo feminino\033[m')
for c in range(0, cont):
    media += cadastrados[c]["idade"]
    if cadastrados[c]["sexo"] == "f":
        print(f'Nome :{cadastrados[c]["nome"]} | Idade {cadastrados[c]["idade"]}')
print(f'\033[33mA media de idade dos cadastrados foi {media/cont:0.0f}\033[m')
print(f'\033[33mCadastros com idade acima da média\033[m')
for c in range(0, cont):
    if cadastrados[c]["idade"] > (media/cont):
        print(f'Nome: {cadastrados[c]["nome"]} | Idade: {cadastrados[c]["idade"]}')