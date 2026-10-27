#%% 
import pandas as pd

clientes = pd.read_csv('../data/clientes.csv', sep =";")
clientes
# %%
# remover as linhas con na é uma possivel solução   
# dropa a linha toda 
clientes = clientes.dropna()
clientes
# %%
# atribuindo especificação ele drop a linha toda de acordo com a atribuição

clientes = clientes.dropna( how = 'any')
clientes
# %%

df = pd.DataFrame(
    {
        "nome": ["Téo", None, "Nah", "Marcio"],
        "idade": [None, None, 43, 52],
        "salario": [3453, 4324, None, 5423]
    }
)

df.dropna(how="all", subset=["idade"])
# %%
df['idade'].fillna(0)  #substitui os dados faltando

# %%
