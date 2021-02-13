print('Programa que gerencia um financiamento de uma casa')
casa = 60000.00
print('\033[35m-=-'*13)
print('\033[35mVENDE-SE UMA CASA NO VALOR DE {:.2f}'.format(casa))
print('\033[35m-=-'*13, end='')
print('\033[m')
print('01 - COMPRAR / 02 - FINANCIAR')
r = int(input('Digite uma opção :'))
if r == 1:
    print('Compra efetuada com sucesso.')
elif r == 2:
    salario = float(input('Qual o seu salário? .'))
    tempo = int(input('Pretende financiar por quanto tempo? .'))
    if casa / tempo + casa / tempo*8/100 > salario*30/100:
        print('Seu financiamento foi negado por exerder R${:.2f} que corresponde a 30% do seu salário'.format(salario*30/100))
    else:
        print('\033[35m-=-' * 13, end='')
        print('\033[m')
        print('Sua casa foi financiada com sucesso em \n{} prestações de R${:.2f} reais,'.format(tempo, (casa / tempo)+(casa / tempo)*8/100))
        print('Taxa de juros de 8% ao mês que acrescentou\n R${:.2f} reais em cada parcela'.format(casa / tempo*8/100))
        print('\033[35m              PARABÉNS'.format(casa))
        print('\033[35m-=-' * 13, end='')
elif r > 2:
    print('\n\033[2;34;0mOPÇÃO ERRADA')