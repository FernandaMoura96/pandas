#%%
import pandas as pd 
df = pd.read_csv('../data/transacao_produto.csv', sep= ';')
df.head()
# %%
filtro = (df['IdProduto']== 5 ) | (df['IdProduto']== 11 )
df[filtro]
# %%
# Vê os nomes exatos de todas as colunas (para detetar espaços escondidos)
print(df.columns)

# Vê o tipo de dados da coluna IdProduto
print(df['IdProduto'].dtype)
# %%
filtro = df["IdProduto"].isin([5,11])
df[filtro]
# %%
