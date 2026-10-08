#%%
import pandas as pd  

idades = [
    22, 35, 19, 42, 51, 28, 64, 33, 25, 47, 
    58, 21, 39, 44, 29, 52, 60, 26, 31, 49, 
    23, 40, 55, 37, 24, 62, 48, 34, 41, 50
]

series_idades = pd.Series(idades)
series_idades
# %%
idades[-1]
idades[0]

#indice da serie
series_idades.iloc[0]
series_idades.iloc[-1]
series_idades[:3]
series_idades[::-1]
# %%
nomes = [
    "Ana", "Beatriz", "Carlos", "Daniel", "Eduarda", 
    "Felipe", "Gabriela", "Heitor", "Isabela", "João", 
    "Larissa", "Lucas", "Mariana", "Nicolas", "Olívia", 
    "Pedro", "Rafaela", "Samuel", "Tatiane", "Vitor", 
    "Alice", "Bruno", "Cecília", "Diego", "Elisa", 
    "Frederico", "Giovanna", "Henrique", "Juliana", "Matheus"
]
series_idades = pd.Series(idades, index = nomes )
series_idades.iloc[-1]
# %%
