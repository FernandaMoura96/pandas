#%%
 
import pandas as pd
import numpy as np

transacoes = pd.read_csv("../data/transacoes.csv", sep = ";")
transacoes.head()

# %%

def diff_amp(x: pd.Series):
    amplitude = x.max() - x.min()
    media = x.mean()
    return np.sqrt((amplitude - media)**2)


def life_time(x:pd.Series):
    dt = pd.to_datetime(x)
    return(dt.max() - dt.min()).days


# %%

idades =pd.Series([
    24, 31, 19, 42, 27, 35, 48, 22, 39, 18, 
    50, 26, 33, 41, 21, 46, 29, 37, 44, 23, 
    30, 40, 25, 47, 34, 19, 43, 28, 36, 49, 
    20, 32, 38, 45, 26])

diff_amp(idades)
# %%

summary = (transacoes.groupby(by=["IdCliente"], as_index=False)
    .agg({
        "IdTransacao": ['count'],
        "QtdePontos": ["sum", "mean", diff_amp],
        "DtCriacao": [life_time]
    })
)

summary.columns = [
    "IdCliente",
    "qtdeTransacao",
    "totalPontos",
    "mediaPontos",
    "ampMeanDiff",
    "lifeTime",
]

summary

# %%
