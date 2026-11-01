#%%
import pandas as pd 

transacoes = pd.read_csv("../data/transacoes.csv", sep = ";")
transacao_produto = pd.read_csv("../data/transacao_produto.csv", sep = ";")
produto = pd.read_csv("../data/produtos.csv", sep = ";")


# %%
transacoes.merge(transacao_produto, 
                 on = 'IdTransacao',
                 how = 'left')
# %%
transacoes.columns 
transacao_produto.columns
# %%
#33m 
