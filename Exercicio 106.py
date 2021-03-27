#Programa que acessa sistema de ajuda em python
while True:
    print('\033[1;7;33m~' * 25)
    print('SISTEMA DE AJUDA PYTHON')
    print('~' * 25)
    f = str(input('\033[mFunção ou Biblioteca >')).lower()
    if f == 'fim':
        print('\033[1;7;95m~' * 12)
        print('  Até logo')
        print('~' * 12)
        break
    tam = len(f)
    print('\033[7;94m~' * (30 + tam))
    print(f'ACESSANDO MANUAL DO COMANDO {f}')
    print('~' * (30 + tam))
    print('\033[7;97m ')
    print(f'{help(f)}')
