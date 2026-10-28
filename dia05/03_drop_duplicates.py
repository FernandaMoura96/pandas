#%%

import pandas as pd

df = pd.DataFrame({
    "nome": ['teo', 'lara', 'nah', 'bia', 'mah', 'lara', 'mah','mah'],
    "sobrenome": ['calvo', 'calvo', 'ataide', 'ataide', 'silva', 'silva', 'silva','silva'],
    "salario": [2132, 1231, 454, 6543, 6532, 4322, 987, 2134],
})

df
# %%
df.drop_duplicates(subset=  ['nome', 'sobrenome'] )
# %%
#deve-se ordenar o dataset antes de dropar, usando o criterio desejado. 
df = (df.sort_values("salario", ascending=False)
      .drop_duplicates(keep='last', subset=["nome", "sobrenome"]))

df

# %%
#seleciona a primeira transação diaria de cada cliente 

transacoes =pd.read_csv("../data/transacoes.csv", sep = ';')
transacoes.columns

transacoes.sort_values("DtCriacao") #ordenar 
transacoes['data'] = pd.to_datetime(transacoes["DtCriacao"]).dt.date #atribuição de data, e somente data
transacoes.drop_duplicates(keep= 'first', subset= ["IdCliente","data" ]) # deduplicar a data com id 
# %%

transacoes.head()

transacoes["data"] = pd.to_datetime(transacoes["DtCriacao"]).dt.date
transacoes = transacoes.sort_values("DtCriacao") 



first = transacoes.drop_duplicates(keep="first", subset=["idCliente", "data"])

last = transacoes.drop_duplicates(keep="last", subset=["idCliente", "data"])
# %%
