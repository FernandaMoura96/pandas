#%%

# O objetivo é encontrar o cliente que tem maior qtd de Streak 

import pandas as pd 

transacoes = pd.read_csv("../data/transacoes.csv", sep = ";")
transacao_produto = pd.read_csv("../data/transacao_produto.csv", sep = ";")
produto = pd.read_csv("../data/produtos.csv", sep = ";")


# %%
cliente_transacao_produto = transacoes.merge(
                transacao_produto, 
                on = 'IdTransacao',
                how = 'left')


# %%
cliente_transacao_produto[['IdTransacao', 'IdProduto','IdCliente']]

# %%

df_full = cliente_transacao_produto.merge(
    produto,
    on= 
    'IdProduto',
)
df_full= df_full[df_full['DescNomeProduto']== "Presença Streak"]

# %%
(df_full.groupby(by= ["IdCliente"])['IdTransacao']
    .count()
    .sort_values(ascending= False)
    .head(1)
)
# %%
# forma mais direta e performatica
# Filtrando o produto diretamente na base correta (produto no singular)
produto_streak = produto[produto['DescNomeProduto'] == "Presença Streak"]

# Executando o pipeline de merge, agrupamento e ordenação
resultado = (
    transacoes.merge(transacao_produto, on="IdTransacao", how="left")
    .merge(produto_streak, on="IdProduto", how="right")
    .groupby(by="IdCliente")["IdTransacao"]
    .count()
    .sort_values(ascending=False)
    .head(1))
resultado 
# %%
