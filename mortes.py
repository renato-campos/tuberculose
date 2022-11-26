# Tratamento dos dados sobre mortes por TB em Santos
import pandas as pd
import matplotlib.pyplot as plt

arquivo = open('.\\landing_area\\mortes_sts.csv', 'r', encoding='ISO-8859-1')
texto = arquivo.readlines()
texto = texto[5:7]
print(texto)

# Criando o dataframe com base nos dados impressos acima
dicionario = {'ano': [2015, 2016, 2017, 2018, 2019, 2020, 2021],
              'morte': [7, 5, 13, 11, 10, 10, 7]}
mortes_df = pd.DataFrame(dicionario)
print(mortes_df)

# gravando o dataframe em csv na staging area
mortes_df.to_csv('.\\staging_area\\mortes.csv', index=False)
arquivo.close()

# criando o gráfico
x = mortes_df['ano']
y = mortes_df['morte']
#plt.style.use('ggplot')
plt.figure(figsize=(10, 5))
plt.ylabel('nº de Mortes', fontsize=16)
plt.yticks([0, 5, 7, 10, 11, 13])
plt.title('Mortes anuais por TB em Santos', fontsize=20)
plt.bar(x, y, color='navy')
plt.show()
