#%%

import pandas as pd 
idades = [
    24, 31, 19, 42, 27, 35, 48, 22, 39, 18, 
    50, 26, 33, 41, 21, 46, 29, 37, 44, 23, 
    30, 40, 25, 47, 34, 19, 43, 28, 36, 49, 
    20, 32, 38, 45, 26
] 
idades =  pd.Series(idades)
idades
# %%
# sumarizando series
idades.sum(),
idades.max(),
idades.min(),
idades.mean(),
idades.describe()

# %%

clientes = pd.read_csv('../data/clientes.csv', sep = ";")
clientes.head()



clientes['flTwitch'].sum()
clientes['flTwitch'].mean()

# %%
social_media = ['flEmail', 'flTwitch', 'flYouTube', 'flBlueSky', 'flInstagram']
clientes[social_media].mean()
# %%
#classificando oque pod ou não pode ser sumarizado 
clientes.dtypes[~(clientes.dtypes ==  'object')].index.tolist()
# %%
num_columns = clientes.dtypes[~(clientes.dtypes ==  'object')].index.tolist() 
clientes[num_columns].mean()
# %%
clientes[num_columns].describe()
# %%
