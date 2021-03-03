#Programa que ler um numero e escreve por estenso
numeros = 'Zero', 'Um', 'Dois', 'Três', 'Quatro,', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze'
while True:
    num = int(input('Digite um numero de 0 a 13 :'))
    if num < 0 or num > 13:
        print('Você digitou numeros fora do intevalo de 0 a 5')
        num = int(input('Digite um numero de 0 a 5 :'))
    print(numeros[num])
