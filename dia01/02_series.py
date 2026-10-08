#%%
import pandas as pd  

idades = [
    22, 35, 19, 42, 51, 28, 64, 33, 25, 47, 
    58, 21, 39, 44, 29, 52, 60, 26, 31, 49, 
    23, 40, 55, 37, 24, 62, 48, 34, 41, 50
]

media = sum(idades) / len(idades)
print("Media:",media)

diffs = 0
for i in idades:
    diffs += (i - media) ** 2

variancia = diffs / (len(idades)-1)

print("Variância:", variancia)

# %%
series_idades = pd.Series(idades)
media = series_idades.mean()
variancia =series_idades.var()
sumary = series_idades.describe()
# %%
# %%
 
