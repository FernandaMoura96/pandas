#%%
import pandas as pd 
# alto explicativo, cabeça e rabo. 

df_lientes =pd.read_csv("../data/clientes.csv", sep = ";")
df_lientes.head(11)
# %%

df_lientes.tail(11)
# %%
# amostra aleaeatória 
df_lientes.sample(11)
# %%
