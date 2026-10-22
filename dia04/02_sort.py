#%% 
#Ordenando colunas 

import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 

clientes = df = pd.read_csv('../data/clientes.csv', sep = ';')
df.head()
# ordenando uma coluna (Serie)
clientes['qtdePontos'].sort_values()
# %%
max_pts = clientes['qtdePontos'].max
filtro =clientes['qtdePontos'] ==  max_pts 

display(clientes[clientes['qtdePontos'] == max_pts])
# %%
#ordenando o dataframe by criterio 
top = (clientes.sort_values(by = 'qtdePontos',ascending= False)
       .head(5)['idCliente'])#pode-se adicionar somente a posição que queremos extrair.

top
# %%
#Sort values para mais de uma classificação 
brinquedo = pd.DataFrame(
    {
        "nome": ["teo", "ana", "nah", "jose"],
        "idade": [32, 43, 35, 42],
        "salario": [2345, 4533, 3245, 4533],
    }
)

brinquedo.sort_values(by= ['salario','idade'], ascending= [False,True])
# %%
