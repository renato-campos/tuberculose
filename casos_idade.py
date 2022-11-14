# Tratamento dos dados relativos aos casos por faixa etária
import pandas as pd
import matplotlib.pyplot as plt

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
del dfgrafico['ano']
plt.style.use('ggplot')
plt.figure(figsize=(10, 4))
plt.title('Casos de TB por Faixa Etária', fontsize=20)
plt.xlabel('Idades', fontsize=14)
plt.ylabel('nº casos', fontsize=14)
plt.xticks(fontsize=14, rotation=45)
plt.plot(dfgrafico.transpose(),'d', markersize=14)
plt.legend(faixa_etaria_df['ano'])
plt.show()
