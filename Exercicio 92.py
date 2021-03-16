#programa que pega dados de entrada de um trabalhador e analisa os dados
from datetime import date, datetime
ano = date.today().year
cliente = {"nome": str(input('Nome :')), "nascimento": int(input('Nascimento :')),}
cliente["idade"] = ano - cliente["nascimento"]
cat = int(input('Carteira de Trabalho :'))
if cat == 0:
    for k, v in cliente.items():
        print(f'{k} tem o valor {v}')
if cat > 0:
    cliente["ctps"] = cat
    ano = int(input('Ano de contratação :'))
    cliente["ano"] = ano
    salario = int(input('Salário :'))
    cliente["salario"] = salario
    cliente["aposentadoria"] = cliente["idade"] + (cliente["ano"] + 35) - datetime.now().year
    print('-' * 30)
    for k, v in cliente.items():
        print(f'    =>{k} tem o valor {v}')
