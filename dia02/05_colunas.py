#%%
import pandas as pd

df = pd.read_csv("../data/transacoes.csv", sep= ";")
df
# %%
df.shape
# %%
df.info(memory_usage='deep')
# %%
df.dtypes
# %%
#RENOMEAR COM UM DICIONARIO. A CHAVE É O NOME ANTIGO, E O VALOR O NOME NOVO

df = df.rename( columns={"QtdePontos": "PtsAcum"})

# PODE-SE RENOMEAR VÁRIAS COLUNAS AO MESMO TEMPO.
#USA-SE inplace=True, PARA NÃO PRECISAR REATRIBUIR O DATAFRAME

# %%
#UMA LISTA ME PERMITE VER SOMENTES AS COLUNAS DESJADAS NO DATAFRAME
#PODE SE USAR DENTRO DE UMA VARIAVEL PARA MELHOR LEGIBILIDADE E ORGANIZAÇÃO

df[["IdCliente","PtsAcum"]]
# %%
#PARA REORDENAS AS COLUNAS, BASTA ALTERAR A ORDEM NA LISTA.
#oU PODE -SE TBM, USAR O .SORT()

colunas = df.columns.tolist()
colunas.sort()
colunas
#APÓS REATRIBUIÇÃO DE ORDENAÇÃO BASTA CHAMAR O DATAFRAME NA POSIÇÃO REORDENADA
df=  df[colunas]
df
# %%
