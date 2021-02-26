#10 primeiros termos de uma Progressão aritimética
print('='*22)
print('\033[33m 10 TERMOS DE UMA PA\033[m')
print('='*22)
n1 = int(input('Digite o primeiro termo :'))
r = int(input('Razão :'))
dec = n1 + (10 - 1) * r
print(dec)
for c in range(n1, dec + r, r):
    print(c, end=' -> ')
print('FIM')
