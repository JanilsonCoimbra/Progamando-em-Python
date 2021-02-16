from time import sleep
print('Contagem regressiva de 10 segundos para a virada de ano')
print('Faltam 10 segundos para a virada')
for c in range(9, 0, -1):
    print(c)
    sleep(1)
print('PARABÉNS, FELIZ ANO NOVO')