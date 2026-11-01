#%%
import pandas as pd

transacoes = pd.read_csv("../data/transacoes.csv", sep= ";")
transacoes.head()
# %%
transacoes.groupby(by = ["IdCliente"]).count()
# %%
transacoes.groupby(by=["IdCliente"], as_index=False)[["IdTransacao"]].count()
# %%
### O que este código faz
###* **`transacoes.groupby(by=["idCliente"], as_index=False)`**: Agrupa os dados do DataFrame `transacoes` por cada cliente (`idCliente`), mantendo o identificador como uma coluna normal e não como o índice do DataFrame
###* **`.agg({...})`**: Aplica operações de agregação específicas para cada coluna
###  * **`"idTransacao": ['count']`**: Conta o total de transações de cada cliente
### * **`"qtdePontos": ['sum', 'mean']`**: Calcula simultaneamente a soma total (`sum`) e a média (`mean`) dos pontos acumulados por cada cliente

summary = (transacoes.groupby(by=["IdCliente"], as_index=False)
 .agg({
     "IdTransacao": ["count"],
     "QtdePontos": ["sum", "mean"]
 })
)
# %%
summary.columns
# %%
summary[('qtdePontos','mean')]

# %%
summary.columns = ['idCliente', 'qtdeTransacao', 'totalPontos', 'avgPontos']
summary
# %%
