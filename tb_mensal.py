import pandas as pd
import matplotlib.pyplot as plt

# tratamento dados crus sobre a TB no Brasil
arquivo = open('.\\landing_area\\casos_br.csv', 'r', encoding='ISO-8859-1')
brasil = arquivo.readlines()
arquivo.close()

# selecionando a parte necessária
brasil = brasil[3:11]
brasil[0] = brasil[0].replace('Ano Diagnóstico', 'ano')

# salvando para staging area
final = open('.\\staging_area\\casos_br.csv', 'w')
final.writelines(brasil)
final.close()

# tratamento dados crus sobre a TB no estado de São Paulo
arquivo = open('.\\landing_area\\casos_spo.csv', 'r', encoding='ISO-8859-1')
saopaulo = arquivo.readlines()
arquivo.close()

# selecionando a parte necessária
saopaulo = saopaulo[4:12]
saopaulo[0] = saopaulo[0].replace('Ano Diagnóstico', 'ano')

# salvando para staging area
final = open('.\\staging_area\\casos_spo.csv', 'w')
final.writelines(saopaulo)
final.close()

# tratamento dados crus sobre a TB em Santos
arquivo = open('.\\landing_area\\casos_sts.csv', 'r', encoding='ISO-8859-1')
santos = arquivo.readlines()
arquivo.close()

# selecionando a parte necessária
santos = santos[4:12]
santos[0] = santos[0].replace('Ano Diagnóstico', 'ano')

# salvando para staging area
final = open('.\\staging_area\\casos_sts.csv', 'w')
final.writelines(santos)
final.close()
