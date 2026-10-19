#%%
import pandas as pd 

df = pd.read_csv('../data/clientes.csv', sep = ';')
df.head()
# %%
df['qtdePontos'] + 100 

# %%
# para somar duas colunas e criar uma nova 
df["flEmail	 flTwitch"] =  df["flTwitch"] + df["flEmail"] 
df.head()
# %%
# para saber a intercecção de duas colunas 

df['Inter']=  df["flTwitch"] * df["flEmail"] 
df.head()
# %%
