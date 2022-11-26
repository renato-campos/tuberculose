import pandas as pd

# tratamento dos dados referente a população de Santos
arquivo = open('.\\landing_area\\pop_sts.csv', 'r', encoding='ISO-8859-1')
texto = arquivo.readlines()
arquivo.close()
texto = texto[4:6]
# print('Santos:\n', texto)

# Criando o dataframe com base no dados saídos na impressão acima
dicionario = {"ano": [2015, 2016, 2017, 2018, 2019, 2020, 2021],
              "pop_sts": [431854, 432231, 432594, 432957, 433311, 433656, 433991]}
pop_sts = pd.DataFrame(data=dicionario)

# tratamento dos dados referentes a população do estado de São Paulo e Brasil
arquivo = open('.\\landing_area\\pop_spo_br.csv', 'r', encoding='ISO-8859-1')
texto = arquivo.readlines()
arquivo.close()
# print('Nacional:\n', texto)

# criando dataframe a partir dos dados saídos
dicionario = {"ano": [2015, 2016, 2017, 2018, 2019, 2020, 2021],
              "pop_spo": [44356304, 44760305, 45149603, 45538936, 45919049, 46289333, 46649132],
              "pop_br": [203475683, 205156587, 206804741, 208494900, 210147125, 211755692, 213317639]}
pop = pd.DataFrame(data=dicionario)

# CRIANDO O DATAFRAME POPULAÇÃO
pop_df = pd.DataFrame()

# incluindo as colunas de população ao dataframe
print("DataFrame dos índice com os dados de população")
pop_df[['ano', 'pop_sts']] = pop_sts[['ano', 'pop_sts']]
pop_df[['pop_spo', 'pop_br']] = pop[['pop_spo', 'pop_br']]
print(pop_df)

# salvar o dataframe só de população
pop_df.to_csv('.\\staging_area\\pop.csv', index=False)
