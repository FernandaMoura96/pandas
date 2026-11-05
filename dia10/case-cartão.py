#%%
import pandas as pd

df = pd.read_csv("transacoes.csv")
df
# %%
# criando coluna como timestamp

df["dtTransacao"] = pd.to_datetime(df["dtTransacao"])
df["vlParcela"] = df["vlVenda"] / df["qtParcelas"]

# Geramos uma lista com os índices das parcelas (0, 1, 2...) para controlar os meses
df["ordemParcela"] = df.apply(
    lambda row: list(range(int(row["qtParcelas"]))), axis=1
)
df_explode = df.explode("ordemParcela")


# %%
def calcDtParcela(row):
    dt = row["dtTransacao"] + pd.DateOffset(months=row["ordemParcela"])
    dt = f"{dt.year} - {dt.month}"
    return dt 

df_explode["dtParcela"] = df_explode.apply(calcDtParcela,
                                                axis=1)

df_explode
# %%
(df_explode.groupby(["idCliente", "dtParcela"])
                    ["vlParcela"].sum()
                    .reset_index()
                    .pivot_table(index = "idCliente",
                                columns= "dtParcela",
                                values = 'vlParcela',
                                fill_value = 0)
)
# %%
