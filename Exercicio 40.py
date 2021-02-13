print('Programa que ler as notas de um aluno, tira média obtida e diz se está aprovado, reprovado ou em recuperação')
n1 = float(input('Digite a primeira nota :'))
n2 = float(input('Digite a segunda nota :'))
media = (n1 + n2) / 2
if media < 5:
    print('Sua média foi {} e você foi CONSERVADO'.format(media))
elif media > 5 and media < 6.9:
    print('Sua media foi {} e você ficou em RECUPERAÇÃO'. format(media))
else:
    print('PARABÉNS, VOCÊ FOI APROVADO COM MÉDIA {} '.format(media))
