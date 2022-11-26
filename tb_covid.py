# Tratamento dos dados relativos aos casos por faixa etária
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# carregando o arquivo de dados de Covid em Santos
covid_df = pd.read_csv('staging_area/covid_sts.csv', sep=';', encoding='ISO-8859-1')
# print(covid_df)

# carregando os dados da TB
tb_df = pd.read_csv('staging_area/casos_sts.csv', sep=';', encoding='ISO-8859-1')
tb_df.rename(columns={'ano' : 'mês'}, inplace = True)
# print(tb_df.loc[5:6])

# criando df com dados covid e tb para 2020 e 2021
dicionario = {"ano": [2020, 2020, 2020, 2020, 2020, 2020, 2020, 2020, 2020, 2020, 2020, 2020, 2021, 2021, 2021, 2021, 2021, 2021, 2021, 2021, 2021, 2021, 2021, 2021],
              "mês": ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez', 'Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez'],
              "TB": [33, 46, 33, 25, 23, 30, 36, 53, 36, 40, 30, 25, 24, 17, 22, 43, 27, 23, 31, 25, 27, 33, 31, 42]}
tb_covid_df = pd.DataFrame(data=dicionario)
tb_covid_df['covid'] = covid_df['covid']
print(tb_covid_df)
