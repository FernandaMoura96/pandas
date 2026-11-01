#%% 
import pandas as pd

df = pd.read_csv("../data/clientes.csv" , sep = ";")
df.head(9)
# %%
#defina uma função a ser aplicada 
def get_last_id(x):
    return x.split("-")[-1] 

#defina a posição de aplicação 
df["idCliente"].apply(get_last_id)

# Guarda o resultado transformado numa nova coluna (ou substitui a antiga)
df["idCliente"] = df["idCliente"].apply(get_last_id)
df.head()
# %%
