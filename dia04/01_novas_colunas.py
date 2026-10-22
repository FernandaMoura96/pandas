#%%
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 

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
df['LogPontos'] = np.log(df['qtdePontos']+1)
df['LogPontos'].describe()
# %%
plt.hist(df['LogPontos'])
plt.grid(True)
plt.show()
# %%
