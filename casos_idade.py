# Tratamento dos dados relativos aos casos por faixa etária
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# carregando o arquivo de dados crus
arquivo = open('.\\landing_area\casos_idade.csv', 'r', encoding='ISO-8859-1')
texto = arquivo.readlines()
arquivo.close()

# extraindo apenas o necessário para a staging area
texto2 = [texto[4]]
for linha in texto[5:12]:
    linha = linha.replace('-', '0')
    texto2.append(linha)
final = open('.\\staging_area\\casos_idade.csv', 'w')
final.writelines(texto2)
final.close()

# carregando o arquivo da staging area para um dataframe
faixa_etaria_df = pd.read_csv('.\\staging_area\\casos_idade.csv', sep=';', encoding='ISO-8859-1')
del faixa_etaria_df['Total']
faixa_etaria_df = faixa_etaria_df.rename(columns={'Ano Diagnóstico': 'ano'})
print(faixa_etaria_df.head(2))
dfgrafico = faixa_etaria_df[:]
dfgrafico.set_index('ano', inplace=True)

# criando o gráfico 
plt.title('Casos de Tuberculose por Faixa Etária', fontsize=14)
plt.ylabel('nº casos')
plt.xlabel('Faixas Etárias')
sns.heatmap(data=dfgrafico, cmap='YlGnBu')
plt.show()
