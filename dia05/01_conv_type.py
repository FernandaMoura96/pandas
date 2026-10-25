#%%
import pandas as pd 

df = pd.read_csv("../data/clientes.csv", sep = ';')
df
# %%
df["qtdePontos"] #verificando tipo de dado 
# %%
df["qtdePontos"].astype(float) #alterando tipo

# %%
#replace substitui atravez de dicionários

df["DtCriacao"] = df["DtCriacao"].replace({
    "0000-00-00 00:00:00.000": "2024-02-01 09:00:00.000"
})

df["DtCriacao"]
# %%
