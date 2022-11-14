import pandas as pd

# tratamento dos dados referente a população de Santos
arquivo = open('.\\landing_area\\pop_sts.csv', 'r', encoding='ISO-8859-1')
texto = arquivo.readlines()
arquivo.close()
texto = texto[4:6]
print('Santos:\n', texto)

# Criando o dataframe com base no dados saídos na impressão acima
dicionario = {"ano": [2015, 2016, 2017, 2018, 2019, 2020, 2021],
              "pop_sts": [431854, 432231, 432594, 432957, 433311, 433656, 433991]}
pop_sts = pd.DataFrame(data=dicionario)

# tratamento dos dados referentes a população do estado de São Paulo e Brasil
arquivo = open('.\\landing_area\\pop_spo_br.csv', 'r', encoding='ISO-8859-1')
texto = arquivo.readlines()
arquivo.close()
print('Nacional:\n', texto)

# criando dataframe a partir dos dados saídos
dicionario = {"ano": [2015, 2016, 2017, 2018, 2019, 2020, 2021],
              "pop_spo": [44356304, 44760305, 45149603, 45538936, 45919049, 46289333, 46649132],
              "pop_br": [203475683, 205156587, 206804741, 208494900, 210147125, 211755692, 213317639]}
pop = pd.DataFrame(data=dicionario)

# carregando dados sobre diagnósticos mensais no Brasil, SP e Santos
tb_mensal_br = pd.read_csv('.\\staging_area\\casos_br.csv', encoding='ISO-8859-1')
tb_mensal_spo = pd.read_csv('.\\staging_area\\casos_spo.csv', encoding='ISO-8859-1')
tb_mensal_sts = pd.read_csv('.\\staging_area\\casos_sts.csv', encoding='ISO-8859-1')

# print(pop_sts, pop, tb_mensal_sts, tb_mensal_spo, tb_mensal_br, sep='\n\n')

# CRIANDO O DATAFRAME PRINCIPAL - ÍnDICES
indice_df = pd.DataFrame()
indice_df[['ano', 'casos_sts']] = tb_mensal_sts[['ano', 'Total']]

indice_df['casos_spo'] = tb_mensal_spo['Total']
indice_df['casos_br'] = tb_mensal_br['Total']

# incluindo as colunas de população ao dataframe principal
indice_df[['pop_sts']] = pop_sts[['pop_sts']]
indice_df[['pop_spo', 'pop_br']] = pop[['pop_spo', 'pop_br']]
print(indice_df)

"""Continuuas a formação do dataframe de índices que está dando erro"""