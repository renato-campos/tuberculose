import pandas as pd
import math
import matplotlib.pyplot as plt
import seaborn as sns

# Carregando os DFs População e de Casos mensais de TB
tb_mensal_df = pd.read_csv('.\\staging_area\\tb_mensal.csv', encoding='ISO-8859-1')
pop_df = pd.read_csv('.\\staging_area\\pop.csv', encoding='ISO-8859-1')
# print(tb_mensal_df, pop_df, sep='\n\n')

# montando o dataframe de indices a partir do pop e tb_mensal
indice_df = pd.merge(tb_mensal_df, pop_df, on='ano')

# calculando os indices de casos por 100k habitantes
indice_df['ind_100k_sts'] = indice_df['casos_sts']/(indice_df['pop_sts']*10**-5)
indice_df['ind_100k_spo'] = indice_df['casos_spo']/(indice_df['pop_spo']*10**-5)
indice_df['ind_100k_br'] = indice_df['casos_br']/(indice_df['pop_br']*10**-5)
print(indice_df)

# criando gráfico de barras triplas dos índices
#plt.style.use('ggplot')
plt.grid(visible=True)
x = indice_df['ano']
y1 = indice_df['ind_100k_br']
y2 = indice_df['ind_100k_spo']
y3 = indice_df['ind_100k_sts']
width = 0.3
plt.xlabel('nº casos TB / 100k habit')
plt.title('Índice de casos TB por 100k habitantes')
plt.barh(x-0.45, y1, width, color='g', )
plt.barh(x-0.15, y2, width, color='r')
plt.barh(x+0.15, y3, width, color='navy')
plt.legend(['Brasil', 'São Paulo', 'Santos'])
plt.show()

#santos_df = indice_df['ano','casos_sts']
variacao = []
for i in range(len(indice_df['casos_sts'])):
    if i != 0:
        variacao.append(math.ceil(1-((indice_df['casos_sts'][i-1] - indice_df['casos_sts'][i]) / indice_df['casos_sts'][i - 1])*100))
    else:
        variacao.append(0)

z1 = indice_df['casos_sts']
z2 = variacao
fig, ax1 = plt.subplots()
plt.title('Casos de TB no período')
plt.ylabel('Total de casos de TB')
ax1.bar(x-0.3, z1, width, color='navy')
ax2 = plt.twinx(ax1)
ax2.bar(x, z2, width, color='r', label='Variação %')
plt.ylabel('Variação %')
plt.yticks([-10,-5,0,5,10,15])
plt.grid()
plt.legend()
plt.show()

