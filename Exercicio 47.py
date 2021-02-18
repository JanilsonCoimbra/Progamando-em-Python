from time import sleep
print('Mostrando numeros pares de 1 até 50')
print('\033[32mOs numeros pares entre 1 e 50 são:\033[m ', end='')
for c in range(2,51,2):
    print(c, end=' ')
    sleep(0.3)



