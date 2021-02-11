print('Programa que pega o nome completo e mostra o primeiro nome e ultimo')
nome = str(input('Digite seu nome completo: ')).strip().split()
print('Seu primeiro nome é {}'.format(nome[0]))
print('Seu ultimo nome é {}'.format(nome[len(nome)-1]))