#%% 

import pandas as pd
# %%

clientes = pd.read_csv('../data/clientes.csv', sep = ';')
clientes.head()
# %%

# gera uma visualialização das linhas onde o filtro = True
# mas não gera uma cópia desse slice do DF 

filtro= clientes['qtdePontos'] ==0
clientes_0 = clientes[filtro].copy() #gera uma cópia identica com endereço distinto
clientes_0['Flag_1'] =1 
clientes_0
# %%
