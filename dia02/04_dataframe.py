#%%
import pandas as pd 
# ALTO EXPLICATIVO, CABEÇA E RABO. 

df_clientes =pd.read_csv("../data/clientes.csv", sep = ";")
df_clientes.head(11) #CABEÇA
# %%

df_clientes.tail(11) #RABO
# %%
# AMOSTRA ALEAEATÓRIA 
df_clientes.sample(11)
# %%
# MOSTRA EM TUPLA A QUANTIDADE DE LINHAS E COLUNAS

df_clientes.shape 
# %%
# SABER O NOME DAS COLUNAS 
df_clientes.columns
# %%
# MOSTRA OS INDICES (as linhas se contam com 1 a menos)
df_clientes.index 
# %%
# INFORMAÇÕES SOBRE DATAFRAME
df_clientes.info()
# %%
# MOSTRA UMA SERIE COM TIPOS ESPECÍFICOS
df_clientes.dtypes 

