#Programa que trata dados de uma tabela do brasilerão
classi = ('Inter', 'Flam', 'Atl-MG', 'SP', 'Flum', 'Palm', 'Grêmio', 'Santos', 'Ath-PR', 'Cor',
                 'Bragan', 'Ceará', 'Atl-GO', 'Sport', 'Fort', 'BH', 'Vasco', 'Goiás', 'Coritiba', 'Botafogo')
print('\033[33mTimes que estão disputando o brasilerão em ordem alfabetica\033[m')
print(sorted(classi))
print('\033[33mClassificação do Brasilerão\033[m')
print(classi)
print('\033[33mOs 5 primeiros colocados\033[m')
print(classi[0:5])
print('\033[33mOs 4 ultimos colocados\033[m')
print(classi[-4:])
print(f'\033[33mO Sport está na posição {classi.index("Sport")} da tabela\033[m')
