#%%
import pandas as pd

df = pd.read_csv("../data/transacoes.csv", sep= ";")
df.head()
# %%
#EXEMPLO PRático
filtro = df['QtdePontos'] >=50
df[filtro]
# %%
#USE & PRA APLICAR MAIS DE UM FILTRO A SERIE
filtro = (df['QtdePontos'] >=50) & (df['QtdePontos'] <100)
filtro
df[filtro]
# %%
# uso do OR(barra vertical  | )
filtro = (df['QtdePontos'] ==1) | (df['QtdePontos'] ==100)
df[filtro]

# %%
#usando dois filtros
filtro = (df["QtdePontos"] > 0) & (df["QtdePontos"] <= 50) & (df["DtCriacao"] >= '2025-01-01')
df[filtro]
# %%
