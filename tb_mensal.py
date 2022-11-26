import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

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

# carregando dados sobre diagnósticos mensais no Brasil, SP e Santos
tb_mensal_br = pd.read_csv('.\\staging_area\\casos_br.csv', sep=';', encoding='ISO-8859-1')
tb_mensal_spo = pd.read_csv('.\\staging_area\\casos_spo.csv', sep=';', encoding='ISO-8859-1')
tb_mensal_sts = pd.read_csv('.\\staging_area\\casos_sts.csv', sep=';', encoding='ISO-8859-1')

#print(tb_mensal_sts, tb_mensal_spo, tb_mensal_br, sep='\n\n')

# CRIANDO O DATAFRAME PRINCIPAL - ÍnDICES
tb_mensal_df = pd.DataFrame()
tb_mensal_df[['ano', 'casos_sts']] = tb_mensal_sts[['ano', 'Total']]
tb_mensal_df[['casos_spo']] = tb_mensal_spo[['Total']]
tb_mensal_df[['casos_br']] = tb_mensal_br[['Total']]


tb_mensal_df.to_csv('.\\staging_area\\tb_mensal.csv', index=False)

# criação dos gráficos
del tb_mensal_sts['Total']
del tb_mensal_spo['Total']
del tb_mensal_br['Total']
tb_mensal_sts = tb_mensal_sts.set_index('ano')
tb_mensal_spo = tb_mensal_spo.set_index('ano')
tb_mensal_br = tb_mensal_br.set_index('ano')
# print(tb_mensal_df, tb_mensal_br, tb_mensal_spo, tb_mensal_sts, sep='\n\n')

# gráficos de calor no casos de TB
sns.heatmap(data=tb_mensal_sts, annot=True, cmap='YlGnBu')
plt.show()
sns.heatmap(data=tb_mensal_spo, cmap='YlGnBu')
plt.show()
sns.heatmap(data=tb_mensal_br, cmap='YlGnBu')
plt.show()

