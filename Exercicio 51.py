#10 primeiros termos de uma Progressão aritimética
print('='*22)
print('\033[33m 10 TERMOS DE UMA PA\033[m')
print('='*22)
n1 = int(input('Digite o primeiro termo :'))
r = int(input('Razão :'))
for c in range(n1, 11, r):
    print(c, end=' -> ')
print('FIM')